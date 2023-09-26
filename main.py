import os
import terminut
import time
import threading
import requests

from os import system
from terminut import printf as print, inputf as input
from time import sleep
from threading import Thread
from requests import post

def start(webhook):
    # Webhook thread start
    for i in range(500):
        print("starting thread")
        t = Thread(target=webhook_spam, args=(webhook,))
        t.start()
        time.sleep(0.1)

def check_webhook(webhook):
    res = requests.get(webhook)
    sc = str(res.status_code)
    if sc.startswith('2'):
        return True
    else:
        return False

def webhook_spam(webhook):
    sent_json = {
        "content": "lol test"
    }
    for i in range(175):
        try:
            r = requests.post(url=webhook, json=sent_json)
            print(f"spammed {r.status_code}")
        except:
            print("webhook paused")
            time.sleep(0.9)

def load():
    print("starting script")
    wh = input("webhook: ")
    if check_webhook(wh):
        print("webhook valid")
        start(wh)
    else:
        print("not a valid webhook")
        starting()

def starting():
    system('cls||CLEAR')
    load()

if __name__ == "__main__":
    starting()
