from playwright.sync_api import sync_playwright

def fetch_items(keyword):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        url = f"https://auctions.yahoo.co.jp/search/search?p={keyword}"
        page.goto(url)

        # 商品一覧が表示されるまで待つ
        page.wait_for_selector("li.Product")

        items = []

        elements = page.query_selector_all("li.Product")
        for elem in elements:
            try:
                # URL
                url = elem.query_selector("a.Product__imageLink").get_attribute("href")

                # タイトル
                title = elem.query_selector("h3.Product__title").inner_text()

                # 価格（現在価格）
                price_text = elem.query_selector("span.Product__priceValue").inner_text()
                price_value = int(price_text.replace("円", "").replace(",", ""))

                items.append({
                    "title": title,
                    "price": price_value,
                    "url": url
                })
            except:
                continue

        browser.close()
        return items

# テスト
#result = fetch_items("Ryzen")
#for item in result:
#    print(item)