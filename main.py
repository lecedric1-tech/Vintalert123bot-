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
        "order": "newest_first",
        "per_page": 5
    }

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json"
    }

    try:
        res = requests.get(url, params=params, headers=headers)

        print("STATUS:", res.status_code)
        print("TEXT:", res.text[:200])

        if res.status_code != 200:
            send(f"❌ HTTP {res.status_code}")
            return

        data = res.json()
        items = data.get("items", [])

        if not items:
            send("⚠️ Aucun résultat")
            return

        for item in items:
            if item["id"] not in seen:
                seen.add(item["id"])

                send(f"🔥 {item['title']}\n💰 {item['price']}€\n👉 {item['url']}")

    except Exception as e:
        send(f"❌ Erreur: {e}")

while True:
    check()
    time.sleep(60)