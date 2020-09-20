from flask import Flask, jsonify
import pymongo
from scrape_mars import scrape
import pandas as pd

#set up Flask app and Mongo server
app = Flask(__name__)
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.mars_db

collection = db.mars_db

#root directory displaying data
@app.route("/scrape")
def home():
    scrape()
    post = {
        "title": scrape.nasa_title,
        "paragraph": scrape,
        "url": scrape.featured_image_url,
        "facts": scrape.mars_facts,
        "hemisphere": scrape.hemisphere_image_urls}
    collection.insert_one
    return "Scraped Mars data, saved to MongoDB!"

#scrape function
@app.route("/scrape")
def home():
    scrape()
    post = {
        "title": scrape.nasa_title,
        "paragraph": scrape,
        "url": scrape.featured_image_url,
        "facts": scrape.mars_facts,
        "hemisphere": scrape.hemisphere_image_urls}
    collection.insert_one
    return "Scraped Mars data, saved to MongoDB!"