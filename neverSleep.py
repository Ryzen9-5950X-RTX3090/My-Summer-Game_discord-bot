from flask import Flask
from threading import Thread
import random
import time
import requests
import logging
app = Flask('')
@app.route('/')
def home():
    return "I am a live Discord bot that stays open 24/7."

def run():
  app.run(host='0.0.0.0',port=random.randint(2000,9000)) 
def ping(target, debug):
    while(True):
        r = requests.get(target)
        if(debug == True):
            print(r.status_code)
        time.sleep(random.randint(30,60)) #alternate ping time between 3 and 5 minutes
def awake(target, debug=False):  
    log = logging.getLogger('werkzeug')
    log.disabled = True
    app.logger.disabled = True  
    t = Thread(target=run)
    r = Thread(target=ping, args=(target,debug,))
    t.start()
    r.start()

def neverSleep():
    t = Thread(target=run)
    t.start()