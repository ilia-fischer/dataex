from os import listdir
from os.path import isfile, join
from pymongo import MongoClient
import json

client = MongoClient('localhost', 27017)
db = client['dataex']
collection = db['datasets']
posts = collection.posts

for post in posts.find():
    print post
