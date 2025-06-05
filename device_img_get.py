import os
import json
import requests
import re

# 保存先ディレクトリ
save_dir = "static/device_imgs"
os.makedirs(save_dir, exist_ok=True)

# JSON読み込み
with open("data/devices.json", encoding="utf-8") as f:
    items = json.load(f)

def safe_filename(name):
    # 日本語・英数・アンダーバーのみ許容
    name = re.sub(r'[^A-Za-z0-9ぁ-んァ-ン一-龥ー_]+', '_', name)
    return name.strip('_')

for item in items:
    url = item["image"]
    # nameをベースにファイル名生成（例: lamzu_maya.jpg）
    ext = url.split('.')[-1].split('?')[0]
    filename = f"{safe_filename(item['name'])}.{ext}"
    save_path = os.path.join(save_dir, filename)

    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            with open(save_path, "wb") as f:
                f.write(r.content)
            print(f"保存成功: {filename}")
        else:
            print(f"取得失敗: {url} ({r.status_code})")
    except Exception as e:
        print(f"エラー: {url} : {e}")
