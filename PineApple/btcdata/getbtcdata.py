import json
import time

import django
import requests

import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'PineApple.PineApple.settings'
django.setup()


def save_btc():
    jsonData = requests.get('https://api.cryptowat.ch/markets/summaries').text

    parsed_json = json.loads(jsonData)

    exchanges = {}
    taco = time.time()
    exchanges['time'] = taco

    max_price = 0
    min_price = 9999999999999999999999999999
    # Go through our json to find btcusd pairs
    for item in parsed_json['result'].keys():
        if item[-6:] == "btcusd":
            # If we find a pair, snag its last price
            price = parsed_json['result'][item]['price']['last']
            exchanges[item] = price
            # Change max or min if found
            if price > max_price:
                max_price = price
            if price < min_price:
                min_price = price

    return exchanges
    # print("Maximum price " + str(max_price) + " USD/BTC. Minimum Price " + str(min_price) + "USD/BTC")
    #
    # # Write data to json
    # with open('../historicaldata/parsedusdbtcdata' + str(taco) + '.json', 'w') as outfile:
    #     json.dump(exchanges, outfile)


if __name__ == "__main__":
    save_btc()
