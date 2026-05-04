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
        "User-Agent": "Mozilla/5.0"
    }

    try:
        res = requests.get(url, params=params, headers=headers)
        data = res.json()

        items = data.get("items", [])

        print("ITEMS:", items)

        if not items:
            send("⚠️ Aucun résultat trouvé")
            return

        for item in items:
            if item["id"] not in seen:
                seen.add(item["id"])

                title = item["title"]
                price = item["price"]
                link = item["url"]

                send(f"🔥 {title}\n💰 {price}€\n👉 {link}")

    except Exception as e:
        send(f"❌ Erreur: {e}")

while True:
    check()
    time.sleep(60)