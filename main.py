import requests
import time

TOKEN = "8787625810:AAHLDdUbsEFf8hjwwTVeIQemGj0lj2juYoo"
CHAT_ID = "8767334604"

seen = set()

SEARCH = "nike dunk 42"

def send(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

def check():
    url = "https://www.vinted.fr/api/v2/catalog/items"
    params = {
        "search_text": SEARCH,
        "order": "newest_first"
    }

    res = requests.get(url, params=params).json()
    items = res.get("items", [])

    for item in items[:5]:
        if item["id"] not in seen:
            seen.add(item["id"])

            title = item["title"]
            price = item["price"]
            link = item["url"]

            send(f"🔥 {title}\n💰 {price}€\n👉 {link}")

while True:
    check()
    time.sleep(60)