# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 20:55:19 2021

@author: icard
"""
from bs4 import BeautifulSoup
from lxml import html
import pandas as pd
import requests
import datetime as dt

#Variables
days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
output = open("anime_schedule.json","w",encoding="utf-8")
series = []

#Retornar el horario de la serie en formato date
def setHour(hour):
    temp = hour.split(":")
    return str(dt.time(int(temp[0]),int(temp[1]),00))

#Obtiene la serie y realiza el proceso de scraping
#Retorna el diccionario de la serie
def getSerie(item):
    #Inicializa el diccionario
    serieDict = {}
    print(item["title"])
    
    #Obitiene información y establece el DOM
    pageContent = requests.get(item["url"])
    pageContent.encoding = "utf-8"
    soup = BeautifulSoup(pageContent.text,"lxml")
    #Busca la información del broadcast
    serieData = soup.find("div",{"id":"content"}).find("td",{"class":"borderClass"}).findAll("div",{"class":"spaceit"})
    #La segunda posición contiene la información del broadcast
    info = serieData[2].text.split()
    
    #Asigna valores al diccionario
    serieDict["title"] = item["title"]
    serieDict["img_url"] = item["image_url"]
    serieDict["synopsis"] = item["synopsis"]
    serieDict["mal_url"] = item["url"]
    
    #Algunas series no cuentan con toda la información del broadcast
    serieDict["day"] = info[1]
    if len(info) == 5:
        serieDict["hour"] = setHour(info[3])
        serieDict["time"] = info[4].replace('(','').replace(')','')
    else:
        serieDict["hour"] = str(dt.time(0,0,0))
        serieDict["time"] = 'Unknown'
    return serieDict

#Obtiene el horario de series que provee la API de Jikan y crea un nuevo diccionario
for day in days:
    req = requests.get('https://api.jikan.moe/v3/schedule/%s' % day)
    print(day)
    if req.status_code == 200:
        res = req.json()
        for item in res[day]:
            series.append(getSerie(item))
    else:
        print("Error en la petición")
        output.close()

data = pd.DataFrame(series)
data.to_json(output,orient="records")
output.close()
print("Fin")