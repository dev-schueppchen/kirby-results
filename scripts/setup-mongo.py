import pymongo

mongo_client = pymongo.MongoClient(
    'mongodb://kirby-ro:D3v5chupp3n@zekro.de:27071/kirby')

mongo_db = mongo_client['kirby']