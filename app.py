from flask import Flask, render_template
import json
from pathlib import Path


app = Flask(__name__)

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
