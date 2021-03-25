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
series = []

def getSerie(item):
    #Inicializa el diccionario
    serieDict = {}
    
    #Obitiene información y establece el DOM
    pageContent = requests.get(item["url"])
    pageContent.encoding = "utf-8"
    soup = BeautifulSoup(pageContent.text,"lxml")
    
    #Busca la información del broadcast
    data = soup.find("div",{"id":"content"}).find("td",{"class":"borderClass"}).findAll("div",{"class":"spaceit"})
    #La segunda posición contiene la información del broadcast
    info = data[2].text.split()
    
    #Asigna valores al diccionario
    serieDict["title"] = item["title"]
    serieDict["img_url"] = item["image_url"]
    serieDict["synopsis"] = item["synopsis"]
    serieDict["mal_url"] = item["url"]
    serieDict["day"] = info[1]
    serieDict["hour"] = info[3]
    serieDict["time"] = info[4].replace('(','').replace(')','')
    return serieDict

for day in days:
    req = requests.get('https://api.jikan.moe/v3/schedule/%s' % day)
    if req.status_code == 200:
        res = req.json()
        for item in res[day]:
            series.append(getSerie(item))
    else:
        print("Error en la petición")

print(series)