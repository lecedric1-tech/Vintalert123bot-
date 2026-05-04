import requests

TOKEN = "TON_TOKEN"
CHAT_ID = "TON_CHAT_ID"

def send(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

def check():
    url = "https://www.vinted.fr/vetements?search_text=nike&order=newest_first&rss=1"

    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X)",
        "Accept": "text/html,application/xhtml+xml",
        "Accept-Language": "fr-FR,fr;q=0.9",
    }

    res = requests.get(url, headers=headers)

    if res.status_code != 200:
        send(f"❌ HTTP {res.status_code}")
        return

    text = res.text

    if "<item>" not in text:
        send("⚠️ Aucun résultat")
        return

    items = text.split("<item>")[1:4]

    for item in items:
        title = item.split("<title>")[1].split("</title>")[0]
        link = item.split("<link>")[1].split("</link>")[0]

        send(f"🔥 {title}\n👉 {link}")

check()