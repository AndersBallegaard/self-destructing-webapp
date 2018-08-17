#!/usr/bin/python3
from flask import Flask
from datetime import datetime, timedelta
from threading import Thread
from os import system
from random import randint

last_load = datetime.now()

def grim_reaper():
    '''
    If site not loaded for 10s reboot host
    reboot can be prevented by calling life_line()
    '''
    s10 = timedelta(seconds=10)
    while True:
        if (last_load + s10) < datetime.now():
            system("reboot")


app = Flask(__name__)


@app.route("/")
def life_line():
    '''
    Save the site from grim_reaper() for 10s
    '''
    global last_load
    last_load = datetime.now()
    return("thank you for saving me for another 10 sec")


if __name__ == "__main__":
    t = Thread(target=grim_reaper)
    t.start()
    app.run(host="0.0.0.0", port=randint(1024,50000), debug=False)