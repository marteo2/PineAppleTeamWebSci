import datetime
import glob

from django.shortcuts import render
import json
import time
import requests

# Create your views here.
from btcdata.getbtcdata import save_btc, find_data


def saveBTC(request):
    jsonData = requests.get('https://api.cryptowat.ch/markets/summaries').text

    parsed_json = json.loads(jsonData)

    print(parsed_json['result']['bitfinex:btcusd'])

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


def index(request):
    # btc_data = save_btc()
    # p = PriceData()
    # p.time = datetime.datetime.fromtimestamp(btc_data["time"]).strftime('%Y-%m-%d %H:%M:%S.%f')
    # p.price = btc_data
    # p.save()

    btc_data = find_data(1524618302.9650571, 1524717699.548168)
    data_points = []
    for i in btc_data.values():
        # print(i)
        data_points.append(i)
    print("end")
    print(data_points)

    if(request.GET and requests.GET["market"]):
        print(request.GET)

    print(time.time())

    return render(request, 'index.html', {"datas": data_points})
