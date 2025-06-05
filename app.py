from flask import Flask, render_template, request
import json
from pathlib import Path


app = Flask(__name__)

@app.after_request
def set_csp(response):
    response.headers["Content-Security-Policy"] = (
        "default-src 'self'; "
        "frame-src https://www.youtube.com https://platform.twitter.com https://*.twitter.com https://clips.twitch.tv https://player.twitch.tv; "
        "script-src 'self' https://platform.twitter.com https://*.twimg.com https://www.instagram.com; "
        "style-src 'self' 'unsafe-inline'; "
        "img-src 'self' data: https://*.twimg.com https://*.instagram.com;"
    )
    return response

@app.route('/')
def index():
    devices = []
    icons = []

    base_dir = Path(__file__).resolve().parent
    devices_path = base_dir / 'data' / 'devices.json'

    if devices_path.exists():
        with devices_path.open() as f:
            devices = json.load(f)


    icons_dir = base_dir / 'static' / 'icons'
    if icons_dir.exists():
        for path in sorted(icons_dir.iterdir()):
            if path.is_file():
                icons.append('/static/icons/' + path.name)

    return render_template('index.html', devices=devices, icons=icons)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
