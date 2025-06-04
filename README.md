# Quromorina Homepage

このリポジトリはラズベリーパイ上で動作する簡単な自己紹介用ホームページのサンプルです。

## 構成
- **Python (Flask)** を用いたシンプルなバックエンド
- HTML/CSS で記述されたフロントエンド

## セットアップ
1. 依存パッケージをインストールします。

```bash
pip install -r requirements.txt
```

2. サーバーを起動します。

```bash
python app.py
```

ブラウザで `http://<ラズパイのIPアドレス>:5000/` にアクセスするとページが表示されます。

## カスタマイズ
- `templates/index.html` を編集し、SNS リンクや使用デバイスのリンクを追加してください。
- スタイルを変更したい場合は `static/styles.css` を編集してください。

