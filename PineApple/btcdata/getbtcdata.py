import ast
import datetime
import json
import time

import django
import requests

import os

from pymongo import *

os.environ['DJANGO_SETTINGS_MODULE'] = 'PineApple.PineApple.settings'
django.setup()


def find_data(start_date, end_date):
    """

    :type end_date: timestamp
    :type start_date: timestamp
    """
    client = MongoClient()

    db = client.websci2018
    btc_collection = db.btcdata_pricedata

    start_date = datetime.datetime.fromtimestamp(start_date)
    end_date = datetime.datetime.fromtimestamp(end_date)
    data = btc_collection.find({"time": {"$gte": start_date, "$lt": end_date}})

    exchanges = {}

    for i in data:
        # print(i["time"])
        # exchanges[i["time"]] = i["time"]
        exchanges[i["time"]] = i["price"]

    return exchanges


def find_data_json(start_date, end_date):
    client = MongoClient()

    db = client.websci2018
    btc_collection = db.btcdata_pricedata

    start_date = datetime.datetime.fromtimestamp(start_date)
    end_date = datetime.datetime.fromtimestamp(end_date)
    data = btc_collection.find({"time": {"$gte": start_date, "$lt": end_date}})
    output = []
    for i in data:
        output.append(ast.literal_eval(i["price"]))
    # output = json.dumps(output)

    return output


def save_btc():
    print("Saving BTC price from cryptowatch")
    jsonData = requests.get('https://api.cryptowat.ch/markets/summaries').text

    parsed_json = json.loads(jsonData)

    exchanges = {}
    taco = time.time()
    exchanges['time'] = taco
    exchanges['price'] = {}

    max_price = 0
    min_price = 9999999999999999999999999999
    # Go through our json to find btcusd pairs
    for item in parsed_json['result'].keys():
        exchange_name = item[-6:]
        # If we find a pair, snag its last price
        price = parsed_json['result'][item]['price']['last']
        if exchange_name not in exchanges["price"]:
            exchanges["price"][exchange_name] = {}
            exchanges["price"][exchange_name][item] = price
        else:
            exchanges["price"][exchange_name][item] = price
        # Change max or min if found
        if price > max_price:
            max_price = price
        if price < min_price:
            min_price = price

    return exchanges


if __name__ == "__main__":
    btc_data = find_data_json(152461830296 / 1000.0, 1524693509569 / 1000.0)
    save_btc()
    print("WOW")
