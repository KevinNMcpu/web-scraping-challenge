#import depdencies
from bs4 import BeautifulSoup
import requests
import pandas as pd

#import headline
url_news = "https://mars.nasa.gov/news/"
r = requests.get(url_news)
soup = BeautifulSoup(r.text, 'html.parser')
nasa_title = soup.find("div", {"class": "content_title"})
nasa_title = nasa_title.get_text()
#get_text still has HTML tags? (/n), so trimming them
nasa_title = nasa_title[2:]
nasa_title = nasa_title[:-3]

#import news summary
nasa_paragraph = soup.find("div", {"class": "rollover_description_inner"})
nasa_paragraph = nasa_paragraph.get_text()
nasa_paragraph = nasa_paragraph[1:]
nasa_paragraph = nasa_paragraph[:-1]

#pull featured image
url_images = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
url_base = "https://www.jpl.nasa.gov"
r2 = requests.get(url_images)
soup2 = BeautifulSoup(r2.text, 'html.parser')
image_url_list = soup2.findAll("a", {"class": "fancybox"})
image_url = image_url_list[2]["data-fancybox-href"]
featured_image_url = url_base + image_url

#pull Mars facts
mars_facts_url = "https://space-facts.com/mars/"
mars_facts = pd.read_html(mars_facts_url)[0]
mars_facts.to_html()

#put hemisphere photos in dict
hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"},
    {"title": "Cerberus Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"},
    {"title": "Schiaparelli Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
    {"title": "Syrtis Major Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"},
]