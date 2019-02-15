# Required modules
import requests
import json
import urllib
import time

# API chat box url link from opening file
read_file = open("API_List.txt", "r")

# Messages that would to follow
wanted_message = ["short", "long", "pump", "dump"]

# Making a function
def messafe_finder(url):
    # Convert to JSON
    data = json.load(urllib.request.urlopen(url))
    for lines in data:
        splited_message = lines["message"].lower().split(" ")
        for item in splited_message:
            if item in wanted_message:
                print("{0} USERNAME : {1} SAID : {2}".format(lines["date"][11:19], lines["user"], lines["message"]))

# Run function while is True every 30 Seconds
while True:
    for line in read_file:
        if line.startswith("URL"):
            messafe_finder(line[5::])
    time.sleep(35)