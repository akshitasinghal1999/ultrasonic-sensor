import time
import RPi.GPIO as GPIO
import urllib
from urllib.request import urlopen
import json


data = urlopen("https://api.thingspeak.com/channels/819879/feeds.json?api_key=879Y7MMUS289HTA0&results=2")

x = data.read()

y = x.decode("utf-8")

z = json.loads(y)

feeds = z["feeds"]
for i in feeds:
    print(i['filds1'])
