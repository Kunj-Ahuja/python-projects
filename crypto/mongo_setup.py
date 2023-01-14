import pymongo
from decouple import config 
url = config('URL')
client = pymongo.MongoClient(url)
db = client['Crypto_Game']
user_db = db['users']
crypto_db = db['crypto']