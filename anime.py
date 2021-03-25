# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 20:55:19 2021

@author: icard
"""
from bs4 import BeautifulSoup
from lxml import html
import pandas as pd
import requests

#days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
days = ["monday"]
for day in days:
    r = requests.get('https://api.jikan.moe/v3/schedule/%s' % day)
    if r.status_code == 200:
        res = r.json()
        for item in res[day]:
            print(item["url"])
            pageContent = requests.get(item["url"])
            pageContent.encoding = "utf-8"
            soup = BeautifulSoup(pageContent.text,"lxml")
            data = soup.find("div",{"id":"content"}).find("td",{"class":"borderClass"}).findAll("div",{"class":"spaceit"})
            print(data[2].text.split())
    else:
        print("Error")

# pc = requests.get('https://myanimelist.net/anime/40028/Shingeki_no_Kyojin__The_Final_Season')
# pc.encoding = "utf-8"
# sp = BeautifulSoup(pc.text,"lxml")
# dt = sp.find("div",{"id":"content"}).find("td",{"class":"borderClass"}).findAll("div",{"class":"spaceit"})
# print(dt[2].text.split())
