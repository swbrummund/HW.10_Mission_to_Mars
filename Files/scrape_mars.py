#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from bs4 import BeautifulSoup
import requests
from splinter import Browser


# # Scrape everything
# 

# In[2]:


# this dictionary will hold everything we pull from all the sites


# In[3]:

def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)


# In[4]:
def scrape():
    browser = init_browser()
    scraped_data = {}
    scraped_data['hemisphere_image_urls'] = []

    # site 1 -
    news_url = "https://mars.nasa.gov/news/" # probably need to replace this since it redirects

    browser.visit(news_url)
    html = browser.html

    # use beautiful soup to parse the url above
    soup = BeautifulSoup(html, 'html.parser')


    # In[5]:


    example_title_div = '<div class="content_title"><a href="/news/8520/nasas-mars-2020-rover-tests-descent-stage-separation/" target="_self">NASAs Mars 2020 Rover Tests Descent-Stage Separation</a></div>'
    example_paragraph_div = '<div class="article_teaser_body">A crane lifts the rocket-powered descent stage away from NASAs Mars 2020 rover after technicians tested the pyrotechnic charges that separate the two spacecraft.</div>'

    # use bs to find() the example_title_div and filter on the class_='content_tile'
    news_title = soup.find('div', class_="content_title").text
    scraped_data['news_title'] = news_title

    # use bs to find() the example_title_div and filter on the class_='article_teaser_body'

    news_p = soup.find('div',class_="article_teaser_body").text
    scraped_data['news_p'] = news_p

    print(news_title)
    print(news_p)


    # In[6]:


    # site 2 - https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars

    # use splinter to connect to the url and navigate, then use bs4 to repeat what you did in site 1
    img_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(img_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    # print(soup.prettify())

    # Example:
    img_source = soup.find('article',class_="carousel_item")["style"]
    print(img_source)


    # In[7]:


    featured_image_home = "jpl.nasa.gov"
    featured_image_url = featured_image_home + img_source.split("'")[1]
    scraped_data['featured_image_url'] = featured_image_url

    featured_image_url


    # In[8]:


    # site 3 - https://twitter.com/marswxreport?lang=en

    # grab the latest tweet and be careful its a weather tweet
    twitter_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(twitter_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    # print(soup.prettify())
    # Example:
    mars_weather = soup.find('div', class_="js-tweet-text-container").text
    scraped_data['mars_weather'] = mars_weather

    print(mars_weather)


    # In[9]:


    # site 4 - 
    facts_url = 'https://space-facts.com/mars/'

    # use pandas to parse the table
    facts_df = pd.read_html(facts_url)[0]
    print(facts_df)

    # convert facts_df to a html string and add to dictionary.
    facts_df_html = facts_df.to_html()
    scraped_data['facts'] = facts_df_html


    # In[10]:


    # site 5 

    # use bs4 to scrape the title and url and add to dictionaryhemisphere_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    hemisphere_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemisphere_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    results = soup.find('div',class_="collapsible results")
    href_results = results.find_all('a',class_='itemLink')

    hemisphere_home = "https://astrogeology.usgs.gov"

    cerberus_url = hemisphere_home + href_results[0]['href']
    schiaparelli_url = hemisphere_home +href_results[2]['href']
    syrtis_url = hemisphere_home +href_results[4]['href']
    valles_url = hemisphere_home +href_results[6]['href']

    print(cerberus_url)
    print(schiaparelli_url)
    print(syrtis_url)
    print(valles_url)


    # In[11]:


    # site 5 
    # use bs4 to scrape the title and url and add to dictionary

    # cerberus_url
    browser.visit(cerberus_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    cerberus = hemisphere_home + soup.find('img',class_="wide-image")['src']
    print(cerberus)

    # schiaparelli_url
    browser.visit(schiaparelli_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    schiaparelli = hemisphere_home + soup.find('img',class_="wide-image")['src']
    print(schiaparelli)

    # syrtis_url
    browser.visit(syrtis_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    syrtis = hemisphere_home + soup.find('img',class_="wide-image")['src']
    print(syrtis)

    # valles_url
    browser.visit(valles_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    valles = hemisphere_home + soup.find('img',class_="wide-image")['src']
    print(valles)

    # Example:
    hemisphere_image_urls = [
        {"title": "Valles Marineris Hemisphere", "img_url": valles},
        {"title": "Cerberus Hemisphere", "img_url": cerberus},
        {"title": "Schiaparelli Hemisphere", "img_url": schiaparelli},
        {"title": "Syrtis Major Hemisphere", "img_url": syrtis},
    ]


    # In[12]:
    scraped_data['hemisphere_image_urls'] = hemisphere_image_urls

    # File-> download as python into a new module called scrape_mars.py
    return scraped_data


# In[ ]:


# use day 3 09-Ins_Scrape_And_Render/app.py as a blue print on how to finish the homework.

# replace the contents of def index() and def scraper() appropriately.

# change the index.html to render the site with all the data.

