import time
from fetcher import fetch_items
from notifier import send_discord_notification

WEBHOOK_URL = "WEBHOOK_URL"


def get_new_items(previous, current):
    previous_url = {item["url"] for item in previous}
    new_items = [item for item in current if item["url"] not in previous_url]
    return new_items


def filter_items(items, min_price, max_price):
    result = []
    for item in items:
        if min_price <= item["price"] <= max_price:
            result.append(item)
    return result

def monitor(keyword, min_price, max_price):
    previous_items = []

    while True:
        print("商品取得中")

        try:
            current_items = fetch_items(keyword)
            filtered_items = filter_items(current_items, min_price, max_price)

        except Exception as e:
            print("取得エラー", e)
            time.sleep(90)
            continue

        new_items = get_new_items(previous_items, filtered_items)

        if new_items:
            print(f"{len(new_items)}件の新着商品を検知")

            for item in new_items:
                send_discord_notification(WEBHOOK_URL, item)

        else:
            print("新着なし")

        previous_items = filtered_items

        time.sleep(90)

min_price = int(input("min price?"))
max_price = int(input("max price?"))
keyword = input("keyword?")

monitor(keyword, min_price, max_price)