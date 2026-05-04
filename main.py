import requests

TOKEN = "TON_TOKEN"
CHAT_ID = "TON_CHAT_ID"

def send(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

def check():
    API_KEY = "TA_CLE"

    target_url = "https://www.vinted.fr/api/v2/catalog/items?search_text=nike&order=newest_first"

    url = f"http://api.scraperapi.com?api_key={API_KEY}&url={target_url}"

    res = requests.get(url)

    try:
        data = res.json()
    except:
        send("❌ Proxy erreur")
        return

    items = data.get("items", [])

    if not items:
        send("⚠️ Aucun résultat")
        return

    for item in items[:5]:
        if item["id"] not in seen:
            seen.add(item["id"])

            send(f"🔥 {item['title']}\n💰 {item['price']}€\n👉 {item['url']}")