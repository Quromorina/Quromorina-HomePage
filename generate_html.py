#!/usr/bin/env python3
"""
GitHub Actions用の動的HTML生成スクリプト
Flaskアプリの機能を再現して静的HTMLを生成
"""

import os
import json
from pathlib import Path

def generate_dynamic_html():
    """動的にHTMLを生成"""
    
    # デバイス情報を読み込み
    devices = []
    devices_path = Path('data/devices.json')
    if devices_path.exists():
        with devices_path.open(encoding='utf-8') as f:
            devices = json.load(f)
    
    # アイコン情報を動的に取得
    icons = []
    icons_dir = Path('static/icons')
    if icons_dir.exists():
        for path in sorted(icons_dir.iterdir()):
            if path.is_file():
                icons.append(f'static/icons/{path.name}')
    
    # HTMLテンプレート
    html_template = '''<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Quromorinaプロフィール</title>
    <link rel="stylesheet" href="static/styles.css">
</head>
<body>
    <header>
        <h1>Quromorinaプロフィール</h1>
    </header>
    <section id="intro">
        <h2>自己紹介</h2>
        <p>ゲームしたりクラブ行ったりしてるオタク。アニメとか漫画とか、映画とか、たまに小説とか見る</p>
    </section>
    <section id="intro">
        <h2>アイコン</h2>
        <p>インターネットでの姿たち</p>
        <div class="intro-icons">
            {icons_html}
        </div>
    </section>
    <section>
        <h2>各種リンク</h2>
        <ul class="social-links">
            <li>
                <a href="https://x.com/Quromorina" target="_new" rel="noopener noreferrer">
                    <img src="static/twitter.png" alt="Twitter icon">Twitter
                </a>
            </li>
            <li>
                <a href="https://www.twitch.tv/quromorina" target="_new" rel="noopener noreferrer">
                    <img src="static/twitch.png" alt="Twitch icon">Twitch
                </a>
            </li>
            <li>
                <a href="https://www.instagram.com/quromorina?igsh=MXI2OW9xeGM1M2tjag==" target="_new" rel="noopener noreferrer">
                    <img src="static/instagram.png" alt="Instagram icon">Instagram
                </a>
            </li>
            <li>
                <a href="https://github.com/Quromorina" target="_new" rel="noopener noreferrer">
                    <img src="static/github.png" alt="GitHub icon">GitHub
                </a>
            </li>
        </ul>
    </section>
    <section>
        <h2>使用デバイス</h2>
        <div class="device-cards">
            {devices_html}
        </div>
    </section>
    <section>
        <h2>最近のプレイリスト</h2>
        <div class="spotify-playlists">
            <div class="spotify-item">
                <iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/23E2XgoNawWCXVo5xYRYdi?utm_source=generator" width="100%" height="352" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
            </div>
            <div class="spotify-item">
                <iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/6H8vyKLDIwiuLN1wa92Yh9?utm_source=generator" width="100%" height="352" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
            </div>
        </div>
    </section>
    <section>
    <h2>おすすめYoutubeコンテンツ</h2>
    <div class="youtube-videos">
        <div class="video-item">
            <iframe src="https://www.youtube.com/embed/qZapP9IwwWU?si=LmXj24yuyMmmkt3K" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
        </div>
        <div class="video-item">
            <iframe src="https://www.youtube.com/embed/JIj7_Rgu2eo?si=XT9Knk7G5kprSrKc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
        </div>
        <div class="video-item">
            <iframe src="https://www.youtube.com/embed/qkWIQ-80EZU?si=muTCJ3ZH6VuDxKSM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
        </div>
        </div>
    </section>

        <footer>
            <p>&copy; 2025 Quromorina</p>
        </footer>
</body>
</html>'''
    
    # アイコンHTMLを生成
    icons_html = '\n            '.join([f'<img src="{icon}" alt="icon">' for icon in icons])
    
    # デバイスHTMLを生成
    devices_html = '\n            '.join([
        f'''<a class="device-card" href="{device['url']}" target="_new" rel="noopener noreferrer">
                <img src="{device['image']}" alt="{device['name']}">
                <p class="device-type">{device['type']}</p>
                <h3>{device['name']}</h3>
            </a>''' for device in devices
    ])
    
    # HTMLを生成
    html_content = html_template.format(
        icons_html=icons_html,
        devices_html=devices_html
    )
    
    # index.htmlに書き込み
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print("動的HTML生成完了!")
    print(f"デバイス数: {len(devices)}")
    print(f"アイコン数: {len(icons)}")

if __name__ == '__main__':
    generate_dynamic_html()
