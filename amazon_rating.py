import requests
from bs4 import BeautifulSoup


def fetch_amazon_rating(url: str) -> str:
    """Return star rating string like '★★★★☆' from an Amazon product page.
    If rating can't be fetched, return 'N/A'."""
    if not url:
        return 'N/A'

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/122.0 Safari/537.36"
        )
    }
    try:
        resp = requests.get(url, headers=headers, timeout=5)
        resp.raise_for_status()
    except requests.RequestException:
        return 'N/A'

    soup = BeautifulSoup(resp.text, 'html.parser')
    span = soup.find('span', {'data-hook': 'rating-out-of-text'})
    if not span:
        span = soup.select_one('span.a-icon-alt')
    if span and span.text:
        text = span.text.strip()
        # e.g. "4.5 out of 5" -> 4.5
        score = text.split()[0]
        try:
            value = float(score)
            # convert 0-5 rating to star symbols
            stars = round(value * 2) / 2  # round to nearest 0.5
            full = int(stars)
            half = 1 if stars - full >= 0.5 else 0
            return '★' * full + ('☆' if half else '') + '☆' * (5 - full - half)
        except ValueError:
            pass
    return 'N/A'
