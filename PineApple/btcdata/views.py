import glob

from django.shortcuts import render


# Create your views here.
def saveBTC(request):
    import json
    import time
    import requests
    jsonData = requests.get('https://api.cryptowat.ch/markets/summaries').text

    parsed_json = json.loads(jsonData)

    print(
    parsed_json['result']['bitfinex:btcusd']
    )
    exchanges = {}
    taco = time.time();
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


def readDATA(request):
    directory = 'historicaldata/'
    import os
    i = 0
    list_of_files = glob.glob('historicadata/*')
    # latest_file = max(list(os.walk(directory)), key=os.path.getctime)
    # print("Lastest File: " + latest_file)
    # for root, dirs, files in reversed(list(os.walk(directory))):
    #     print(root, dirs, files)
    #     # print(files[0:5])
    #
    # pass


def index(request):
    saveBTC(request)
    readDATA(request)
    return render(request, 'btcdata/index.html')
