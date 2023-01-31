import pymongo
url = 'mongodb+srv://replit:replit_password@cluster0.yrlml0x.mongodb.net/?retryWrites=true&w=majority'
client = pymongo.MongoClient(url)
db = client['Crypto_Game']
user_db = db['users']
crypto_db = db['crypto']