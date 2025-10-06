# Quromorinaプロフィールサイト

ゲームしたりクラブ行ったりしてるオタクのプロフィール

## 🚀 機能

- **自己紹介**: プロフィール情報
- **使用デバイス**: 動的に読み込まれるデバイス一覧
- **各種SNSリンク**: Twitter、Twitch、Instagram、GitHub
- **Spotifyプレイリスト**: 埋め込みプレイリスト
- **おすすめYouTubeコンテンツ**: 埋め込み動画

## 🔄 動的サイト生成

このサイトは**GitHub Actions**を使用して動的に生成されます：

### 自動実行タイミング
- **プッシュ時**: コードをプッシュするたびに自動実行
- **定期実行**: 毎日午前2時に自動実行
- **手動実行**: GitHubのActionsタブから手動実行可能

### 動的要素
- **デバイス情報**: `data/devices.json`から自動読み込み
- **アイコン**: `static/icons/`フォルダから自動検出
- **画像更新**: `device_img_get.py`でデバイス画像を自動更新

## 📁 ファイル構成

```
├── index.html              # メインページ（動的生成）
├── generate_html.py        # HTML生成スクリプト
├── device_img_get.py       # デバイス画像取得スクリプト
├── data/
│   └── devices.json        # デバイス情報
├── static/                 # 静的ファイル
│   ├── styles.css          # CSS
│   ├── device_imgs/        # デバイス画像
│   ├── icons/              # アイコン画像
│   └── *.png               # SNSアイコン
├── .github/workflows/      # GitHub Actions
│   └── dynamic-site.yml    # 動的サイト生成ワークフロー
└── _config.yml             # Jekyll設定（GitHub Pages用）
```

## 🛠️ ローカル開発

### 静的サイトとして実行
```bash
# Python 3の場合
python -m http.server 8000

# Node.jsの場合
npx serve .
```

### 動的HTML生成
```bash
# デバイス画像を更新
python device_img_get.py

# HTMLを動的生成
python generate_html.py
```

## 🌐 GitHub Pagesでのデプロイ

1. **リポジトリのSettings → Pages**
2. **Source**: "Deploy from a branch"
3. **Branch**: "main"
4. **Folder**: "/ (root)"

数分後、以下のURLでアクセス可能：
`https://quromorina.github.io/Quromorina-HomePage/`

## 🔧 カスタマイズ

### デバイス情報を追加
`data/devices.json`に新しいデバイス情報を追加すると、自動でサイトに反映されます。

### アイコンを追加
`static/icons/`フォルダに画像を追加すると、自動でアイコンセクションに表示されます。

## 📝 技術スタック

- **静的サイト**: HTML + CSS
- **動的生成**: Python + GitHub Actions
- **ホスティング**: GitHub Pages
- **自動化**: GitHub Actions

## 🎯 特徴

- **完全無料**: GitHub Pages + GitHub Actions
- **自動更新**: データ変更時に自動でサイト更新
- **高速配信**: 静的サイトで高速アクセス
- **動的要素**: データに基づく動的コンテンツ生成