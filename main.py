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
    send("🚀 BOT ACTIF")

while True:
    check()
    time.sleep(60)