from flask import Flask, request, render_template
import json
from dotenv import load_dotenv     # for loading environment variables
import os
import pymongo                     # for MongoDB connection (ATLAS)

load_dotenv()

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

MONGO_URI = os.getenv("MONGODB_URI")

# Create a new client and connect to the server
client = MongoClient(MONGO_URI, server_api=ServerApi('1'))

db = client.test

# Create a collection
collection = db['flask_tutorial']

app = Flask(__name__)       #creating Flask app

@app.route('/')
def home():
    return render_template('index.html')    #for showing form via index.html

@app.route('/submit', methods=['POST'])
def submit():
    form_data = dict(request.form)  # Get form data as a dictionary
    # Insert the form data into the MongoDB collection
    collection.insert_one(form_data)
    return 'Data submitted successfully.'
if __name__ == '__main__':
    app.run(debug=True)     # Run the app in debug mode