import requests
import time

# API chat box url link from opening file
read_file = open("API_List.txt", "r")

#Print BITMEX_ADA_LAST_PRICE_
def price_print(url):
    # Convert to HTML text
    html_data = requests.get(url).text
    # Find ADA Price; That is in 1 list section
    ada_price = (html_data.split("ADAH19")[1].split("lastPrice"))[1][2:-2]
    print("BITMEX_ADA_LAST_PRICE_:", ada_price)

while True:
    for line in read_file:
        if line.startswith("LP"):
            price_print(line[5::])
    time.sleep(10)