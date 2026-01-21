import requests

def send_discord_notification(webhook_url, item):
    message = {
        "content" : f"新着商品検知\n"
                    f"**{item["title"]}**\n"
                    f"価格：{item["price"]} 円\n"
                    f"URL: {item["url"]}"
    }
    requests.post(webhook_url, json=message)