from flask import Flask, jsonify
from flask_pymongo import PyMongo
from scrape_mars import scrape
import pandas as pd

#set up Flask app and Mongo server
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017/"
mongo = PyMongo(app)

#scrape function
@app.route("/scrape")
def home():
    scrape()
    print(scrape.nasa_title)
    print(scrape.nasa_paragraph)
    mongo.save_file("title", scrape.nasa_title)
    mongo.save_file("paragraph", scrape.nasa_paragraph)
    mongo.save_file("url", scrape.featured_image_url)
    mongo.save_file("facts", scrape.mars_facts)
    mongo.save_file("hemisphere", scrape.hemisphere_image_urls)
    return "OK"