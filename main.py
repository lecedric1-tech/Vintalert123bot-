import requests
import time

TOKEN = "8787625810:AAHLDdUbsEFf8hjwwTVeIQemGj0lj2juYoo"
CHAT_ID = "8767334604"

seen = set()

search = "nike"

def send(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

def check():
    url = "https://www.vinted.fr/vetements?search_text=nike&order=newest_first&rss=1"

    try:
        res = requests.get(url)
        text = res.text

        if "<item>" not in text:
            send("⚠️ Aucun résultat RSS")
            return

        items = text.split("<item>")[1:6]

        for item in items:
            title = item.split("<title>")[1].split("</title>")[0]
            link = item.split("<link>")[1].split("</link>")[0]

            if link not in seen:
                seen.add(link)

                send(f"🔥 {title}\n👉 {link}")

    except Exception as e:
        send(f"❌ Erreur: {e}")

while True:
    check()
    time.sleep(60)