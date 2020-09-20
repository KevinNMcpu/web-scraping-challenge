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
@app.route("/")
def home():
    scrape()
    url1 = scrape.hemisphere_image_urls[0]['img_url']
    url2 = scrape.hemisphere_image_urls[1]['img_url']
    url3 = scrape.hemisphere_image_urls[2]['img_url']
    url4 = scrape.hemisphere_image_urls[3]['img_url']
    return (
            f'<body style="font-family:Calibri">'
            f'<p style="font-family:Calibri;font-size:80px;margin-top: 1em;margin-bottom: 1em;text-align: center">Mission To Mars!</p>'
            f'<p style="font-family:Calibri;font-size:40px;margin-top: 0em;margin-bottom: 0em">Latest Mars News</p>'
            f'<p style="font-family:Calibri;font-size:20px;margin-top: 0em;margin-bottom: 0em">{scrape.nasa_title}</p>'
            f'<p style="font-family:Calibri;margin-top: 0em;margin-bottom: 0em">{scrape.nasa_paragraph}</p>'
            f'<table>'
            f'<tr>'
            f'<th><p style="font-family:Calibri;font-size:40px;margin-top: 0.5em;margin-bottom: 0em">Featured Mars Image</p></th>'
            f'<th><p style="font-family:Calibri;font-size:40px;margin-top: 0.5em;margin-bottom: 0em">Mars Facts</p></th>'
            f'</tr>'
            f'<tr>'
            f'<td><img src="{scrape.featured_image_url}" width="400" height="auto"></td>'
            f'<td>{scrape.mars_facts.to_html(index=False, header=False)}</td>'
            f'</tr>'
            f'</table>'
            f'<p style="font-family:Calibri;font-size:40px;margin-top: 1em;margin-bottom: 1em;text-align: center">Mars Hemispheres</p>'
            f'<table>'
            f'<tr><td><img src="{url1}" width="400" height="auto"></td><td><img src="{url2}" width="400" height="auto"></td></tr>'
            f'<tr><td>Valles Marineris Hemisphere</td><td>Cerberus Hemisphere</td></tr>'
            f'<tr><td><img src="{url3}" width="400" height="auto"></td><td><img src="{url4}" width="400" height="auto"></td></tr>'
            f'<tr><td>Schiaparelli Hemisphere</td><td>Syrtis Major Hemisphere</td></tr>'
            f'</table>'
            f'</body>'
    )

#scrape function
@app.route("/scrape")
def data():
    scrape()
    post = {
        "title": scrape.nasa_title,
        "paragraph": scrape.nasa_paragraph,
        "url": scrape.featured_image_url,
        "facts": scrape.mars_facts,
        "hemisphere": scrape.hemisphere_image_urls}
    collection.insert_one
    return "Scraped Mars data, saved to MongoDB!"