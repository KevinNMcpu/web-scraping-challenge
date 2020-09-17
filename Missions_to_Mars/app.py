from flask import Flask, jsonify
from flask_pymongo import PyMongo
from scrape_mars import scrape
import pandas as pd

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017/"
mongo = PyMongo(app)

@app.route("/scrape")
def home():
    scrape()
    print(scrape.nasa_title)
    print(scrape.nasa_paragraph)
    return ()
