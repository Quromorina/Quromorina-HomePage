# Quromorinaプロフィールサイト

ゲームしたりクラブ行ったりしてるオタクのプロフィールサイトです。

## 機能

- 自己紹介
- 使用デバイス一覧
- 各種SNSリンク
- Spotifyプレイリスト
- おすすめYouTubeコンテンツ

## GitHub Pagesでのデプロイ

このサイトはGitHub Pagesでホスティングされています。

### デプロイ手順

1. このリポジトリをGitHubにプッシュ
2. リポジトリのSettings > Pagesでソースを「Deploy from a branch」に設定
3. Branchを「main」に設定
4. 数分待つとサイトが公開されます

### ローカル開発

静的サイトなので、ブラウザで直接`index.html`を開くか、簡単なHTTPサーバーを使用：

```bash
# Python 3の場合
python -m http.server 8000

# Node.jsの場合
npx serve .
```

## ファイル構成

```
├── index.html          # メインページ
├── static/             # 静的ファイル
│   ├── styles.css      # CSS
│   ├── device_imgs/    # デバイス画像
│   └── icons/          # アイコン画像
└── _config.yml         # Jekyll設定（GitHub Pages用）
```