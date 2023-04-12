from flask import Flask, jsonify, request
from bson import ObjectId

# Import database
from db import db

# Create Flask app to connect front-end, back-end, and database
app = Flask(__name__)


# Part 1: App test - Does not use the database
@app.route("/")
def flask_mongodb_atlas():
    return "Flask App created and running"


# Part 2: Test API - Insert random hard-coded data to test connection to database
@app.route("/test")
def test():
    db.collection.insert_one({"name": "Jay"})
    return "Connected to the database!"


# Part 3: API to return all recipes currently stored in the database
@app.route("/get-all")
def get_all():
    # Collect all the data from the database
    all = db.collection.find()

    # For each document, convert _id from type ObjectId to string so it can be JSON serializable
    data = []
    for doc in all:
        doc["_id"] = str(doc["_id"])
        data.append(doc)

    # Return as JSON type
    return jsonify(data)


# Part 4: API to insert one recipe into the database
@app.route("/insert-one", methods=["POST"])
def insert_one():
    input_json = request.get_json()
    # this serves as a crude check that all the fields we need are in the
    # request payload, and that we're not entering erroneous entries either
    dict_to_return = {
        "name": input_json["name"],
        "ingredients": input_json["ingredients"],
        "method": input_json["method"],
    }
    db.collection.insert_one(dict_to_return)
    # the above call mutates dict_to_return to include the ID of the new entry
    # in the DB. Data of ObjectID type can't be parsed by the browser, so we 
    # convert it to a string
    dict_to_return["_id"] = str(dict_to_return["_id"])
    return dict_to_return


# Part 5: API to remove one recipe from the database using the recipe's ID
# e.g. body might be {"_id": "63089f6c32adbaebfa6e8d06"}
@app.route("/remove-one", methods=["DELETE"])
def remove_one():
    input_json = request.get_json()

    # Convert string back to MongoDB ObjectId type
    dict_to_query = {"_id": ObjectId(input_json["_id"])}

    # Remove from database
    db.collection.delete_one(dict_to_query)
    return f"successfully deleted {dict_to_query['_id']}"


if __name__ == "__main__":
    app.run(port=8000, debug=True)
