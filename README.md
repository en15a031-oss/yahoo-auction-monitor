Yahoo!オークション 新着商品監視ツール

1. 概要
このツールは、Yahoo!オークションの検索結果を定期的に取得し、新着商品を検知して Discord に自動通知する監視システムです。

Playwright を用いた安定したスクレイピング、  
価格フィルター、差分検知、Webhook 通知など、  
実運用を意識した構成になっています。


2. 特徴

●Playwrightによるスクレイピング
Yahoo!オークションの検索結果ページを自動取得し、  
商品タイトル・価格・URL を抽出します。

●差分検知で「新着のみ」通知
前回取得した商品リストと比較し、  
新しく出品された商品だけを検出します。

●価格フィルター機能
通知対象を価格帯で絞り込み、  
ノイズの少ない実用的な監視が可能です。

●Discord Webhook 通知
検知した新着商品を Discord に自動送信します。

●90秒間隔の監視ループ
Yahoo!側の負荷やアクセス制限を考慮した監視間隔:90秒で動作します。

---

3.ディレクトリ構成
yahoo-auction-monitor/
├── fetcher.py      # Playwright を使った商品取得 ├── notifier.py     # Discord 通知処理
├── monitor.py      # 監視ループ
├── requirements.txt    # 依存パッケージ
└── README.md

4.使い方
<1> リポジトリを clone
<2> 依存パッケージをインストール
    pip install -r requirements.txt
    playwright install
<3> Discord Webhook URL を設定
    `monitor.py` の以下の部分を書き換えます。
    WEBHOOK_URL = "あなたのWebhook URL"
<4> 実行
    起動後、以下を入力します。
    - min price
    - max price
    - keyword

