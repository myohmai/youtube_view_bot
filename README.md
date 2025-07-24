# YouTube View Tracker Discord Bot 🎥🤖

このBotは、指定されたYouTube動画の再生回数を定期的に取得し、Discordのチャンネルに再生回数や達成メッセージを投稿するものです。

## 🔧 機能概要

- 特定のYouTube動画の再生回数を定期取得
- Discordに自動で埋め込みメッセージ送信（embed）
- 再生回数が目標（例：800万回、900万回など）を超えると達成メッセージを表示
- `.env` で環境変数管理
- `config.py` で動画・チャンネル設定を管理

## 🗂 ディレクトリ構成（例）
youtube_tracker_bot/
├── main.py
├── youtube_api.py
├── config.py
├── goals.json
├── .env
├── .gitignore
└── README.md

- `.env`: DiscordのトークンやYouTube APIキー
- `config.py`: 動画ID・DiscordチャンネルID・目標回数をまとめた設定ファイル
- `youtube_api.py`: 再生回数と動画タイトル・サムネを取得する処理
- `main.py`: Botの本体（通知処理）
- `goals.json`: キリの良い再生数を超えたかどうかの記録


## 🛠 使用方法

1. `.env` ファイルを作成し、次のように記述：

```env
DISCORD_TOKEN=あなたのDiscordBotトークン
YOUTUBE_API_KEY=あなたのYouTube APIキー

ResplitではSecretsに格納

2.	config.py に対象の動画IDとDiscordチャンネルIDを設定：

VIDEOS = [
    {
        "video_id": "XXXXXXXXXXX",
        "channel_id": 123456789012345678,
        "goal": 8000000
    },
    ...
]

3.	実行（Python 3.10〜を推奨）

python main.py

✅ 備考
	•	Botは午前8時〜午後10時の間のみ投稿する仕様です。
	•	Resplit UptimeRobot Flask などの外部サーバーに設置して定期実行できます。
	•	goals.json は再生数の達成管理に使われます（自動生成）。

✅ Discord のチャンネル ID を取得する方法
	1.	Discord を開く
	2.	「ユーザー設定」 → 「詳細設定」 → 「開発者モード」をオン
	3.	対象チャンネル名を右クリック → 「IDをコピー」

⸻

✅ Bot をサーバーに招待する方法
	1.	Discord Developer Portal へアクセス
	2.	作成したアプリを選択
	3.	左側メニューの「OAuth2」 → 「URL Generator」へ移動
	4.	以下を選択：
	•	Scopes: bot
	•	Bot Permissions: Send Messages, Embed Links, Read Message History など必要な権限
	5.	生成された URL を開いて、Bot を自分のサーバーに招待する


## 動画を追加したいとき
- `config.py` に動画IDとDiscordチャンネルIDを追加するだけ

## 停止したいとき
- または `.env` を一時的にリネーム

	•	GitHubリポジトリはプライベートです
	•	クローンやプルするときはGitHubの認証（SSHキーやアクセストークン）が必要です
