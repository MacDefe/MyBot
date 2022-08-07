import pymongo

client = pymongo.MongoClient('mongodb://localhost/nikitosik_bot_piuoy_bot')
users_db = client.get_database()["users_db"]