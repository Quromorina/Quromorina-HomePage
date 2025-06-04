from flask import Flask, render_template
import json
from pathlib import Path


app = Flask(__name__)

@app.route('/')
def index():
    devices = []
    media = {}
    icons = []

    base_dir = Path(__file__).resolve().parent
    devices_path = base_dir / 'data' / 'devices.json'
    media_path = base_dir / 'data' / 'media.json'

    if devices_path.exists():
        with devices_path.open() as f:
            devices = json.load(f)

    if media_path.exists():
        with media_path.open() as f:
            media = json.load(f)

    icons_dir = base_dir / 'static' / 'icons'
    if icons_dir.exists():
        for path in sorted(icons_dir.iterdir()):
            if path.is_file():
                icons.append('/static/icons/' + path.name)

    return render_template('index.html', devices=devices, media=media, icons=icons)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
