from flask import Flask, render_template
import json
from pathlib import Path

from amazon_rating import fetch_amazon_rating

app = Flask(__name__)

@app.route('/')
def index():
    devices = []
    media = {}

    devices_path = Path('data/devices.json')
    media_path = Path('data/media.json')

    if devices_path.exists():
        with devices_path.open() as f:
            devices = json.load(f)

        for item in devices:
            if item.get('amazon_url'):
                rating = fetch_amazon_rating(item['amazon_url'])
                if rating != 'N/A':
                    item['rating'] = rating

    if media_path.exists():
        with media_path.open() as f:
            media = json.load(f)

    return render_template('index.html', devices=devices, media=media)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
