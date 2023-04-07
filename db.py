from flask import Flask
from flask_pymongo import pymongo

# TO BE FILLED BY USER
CONNECTION_STRING = ""

# Create user that sends/receives requests
client = pymongo.MongoClient(CONNECTION_STRING)

# Find or create database
db = client.get_database('flask_mongodb_recipes')

# Create a collection (JSON format dict) within the database
collection = pymongo.collection.Collection(db, 'collection')