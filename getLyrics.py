#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 23:11:53 2018

@author: nojan
"""

import requests
from bs4 import BeautifulSoup as bs4
import credentials

url = "https://api.spotify.com/v1/me/player/currently-playing"
headers = {"Accept": "application/json", "Content-Type": "application/json",
           "Authorization": 
               "Bearer " + credentials.spotifyCurrentPlay}
r = requests.get(url, headers=headers)
song = r.json()
name = song["item"]["name"]
artist = song["item"]["artists"][0]["name"]

#%%
param = name + " " + artist
param = '%20'.join(param.split(" "))
url = "https://api.genius.com/search?q="+param
headers = {"Authorization": 
               "Bearer " + credentials.geniusSearch}

lyrics = requests.get(url, headers=headers)
lyrics = lyrics.json()

pageUrl = "https://genius.com"+lyrics["response"]["hits"][0]["result"]["path"]
page = requests.get(pageUrl)
html = bs4(page.text, "lxml")
for line in html('script'):
    line.extract()
final = html.find('div', class_='lyrics').get_text()

print(final)