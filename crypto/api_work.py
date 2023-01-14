import requests
from mongo_setup import crypto_db

url = 'https://api.binance.com/api/v3/ticker/price?symbol='
currencies = {
    "BTCUSDT": 'BTC', 
    "DOGEUSDT": 'DOGE', 
    "LTCUSDT": 'LTC',
    'ETHUSDT': 'ETH'
    }

a = 0
while a < len(currencies):
    for i in currencies:
        key = url+i
        data = requests.get(key)  
        data = data.json()
        price_data = {
            'name' : currencies[i],
            'price' : round(float(data['price']),4)
        }
        if crypto_db.find_one({'name' : currencies[i]}):
            newData = { '$set' : { 'price' : round(float(data['price']),4)}}
            oldData = {'name' : currencies[i]}
            crypto_db.update_one(oldData,newData)
        else:
            crypto_db.insert_one(price_data)
        a = a+1