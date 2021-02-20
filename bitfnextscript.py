import requests
import time
from datetime import datetime, timezone
import sched, time
import time
from tqdm import tqdm

influxURL = 'http://localhost:8086'
serverURL = 'https://api-pub.bitfinex.com/v2'
dbName = 'test8'

"""
    @getTickerInfoAll - getting information about tickets

"""
def getTickerInfoAll():
    req = requests.get('https://api-pub.bitfinex.com/v2/tickers?symbols=ALL')
    return req
"""
    @createQuery - create database
    
"""
def createQuery():
    from influxdb import InfluxDBClient
    client = InfluxDBClient(host='localhost', port=8086)
    client.create_database(dbName)
headers = {
    'format': 'application/json',
    'type': 'application/x-www-form-urlencoded',
    'coding': 'gzip'
}     
class parseAndWrite :
    """
    @httpWrite - data recdrding via /write
    
    """
    def httpWrite(self, payload):
        influxWriteURL = influxURL + '/write?' + 'db=' + dbName + '&precision=s'
        req = requests.post(influxWriteURL, headers=headers, data=payload)
        return req
    """
    @httpWrite - parsing
    
    """
    def fuckingParse(self, fuckingLists):
        line = ''
        for fuckingList in fuckingLists:
            if(fuckingList[0][0] == 't'):
                symbol, bid, bidSize, ask, askSize, dailyChange, dailyChangeRelative, lastPrice, volume, high, low = fuckingList
                InlineQuery += f'{dbName},pair={symbol} bid={bid},bid_size={bidSize},ask={ask},ask_size={askSize},daily_change={dailyChange},daily_change_rel={dailyChangeRelative},last_price={lastPrice},volume={volume},high={high},low={low}\n'
        return line
while True:
    """
    @httpWrite - function calls
    
    """
    fuckingInflux = parseAndWrite()
    getTickerInfoAll()
    fuckingTikcersList = getTickerInfoAll()
    createQuery()
    result = fuckingInflux.fuckingParse(fuckingTikcersList.json())
    data = fuckingInflux.httpWrite(result)
    #print(result)
    print('Loading...')
    for i in tqdm(range(10)):
        time.sleep(1)
    time.sleep(10)