import os
from pymongo import MongoClient

MONGO_URI = 'mongodb://localhost:27017'

client = MongoClient(MONGO_URI)

items_db = client["fast_api"]
items_collection = items_db["items"]
