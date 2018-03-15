# pprint.pprint(jsonData)
# for channel in jsonData..values():
#     print(
#     channel ) # prints the entire channel
#     print(
#     channel['name'] )# prints name
# print(jsonData.allowance)
import json
import time
import requests


def savebtc():
    jsonData = requests.get('https://api.cryptowat.ch/markets/summaries').text

    parsed_json = json.loads(jsonData)

    # print(
    # parsed_json['result']['bitfinex:btcusd']
    # )
    exchanges = {}
    taco = time.time()
    exchanges['time'] = taco

    max = 0
    min = 9999999999999999999999999999
    # Go through our json to find btcusd pairs
    for item in parsed_json['result'].keys():
        if (item[-6:] == "btcusd"):
            # If we find a pair, snag its last price
            price = parsed_json['result'][item]['price']['last']
            print(item + " " + str(price))
            exchanges[item] = price
            # Change max or min if found
            if (price > max):
                max = price
            if (price < min):
                min = price

    print("Maximum price " + str(max) + " USD/BTC. Minimum Price " + str(min) + "USD/BTC")

    # Write data to json
    with open('historicaldata/parsedusdbtcdata' + str(taco) + '.json', 'w') as outfile:
        json.dump(exchanges, outfile)
    print("Saved btc data to file")
