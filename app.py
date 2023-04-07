from flask import Flask, jsonify, request
from bson import ObjectId

# Import database
from db import db

# Create Flask app to connect front-end, back-end, and database
app = Flask(__name__)

# Part 1: App test - Does not use the test
@app.route('/')
def flask_mongodb_atlas():
    return "Flask App created and running"

# Part 2: Test API (send/put) - Insert random data
@app.route('/test')
def test():
    db.collection.insert_one({
        "name" : "Jay"
    })
    pass

# Part 3: Return all to make sure reader works right
@app.route('/get-all')
def getAll():
    # Collect all the data from the database
    all = db.collection.find()
    
    # For each document, convert object id to string type so it can be comprehensible by the compiler
    data = []
    for doc in all:
        doc['_id'] = str(doc['_id'])
        data.append(doc)
    
    # Return as JSON type
    return jsonify(data)

