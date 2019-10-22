from flask import Flask
import pymongo 
import os
import dns
from config import Config
from pymongo import MongoClient
from bson.objectid import ObjectId


client = pymongo.MongoClient(Config.MONGO_URI)
db = client.myTestDB

DBS_NAME = "myTestDB"
COLLECTION_NAME = "myFirstMDB"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(Config.MONGO_URI)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e
        
conn = mongo_connect(client)

coll = conn[DBS_NAME][COLLECTION_NAME]


coll.update_many({'nationality': 'american'}, {'$set': {
    'hair_colour': 'maroon'
}})

documents = coll.find({'nationality' : 'american'})

for doc in documents:
    print(doc)

