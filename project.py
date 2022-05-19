from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import requests
import pandas as pd
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page=requests.get(START_URL)
soup=BeautifulSoup(page.text,"html.parser")
star_table=soup.find("table")
tlist=[]
table_rows=star_table.find_all("tr")
for tr in table_rows:
    td=tr.find_all("td")
    row=[i.text.rstrip()for i in td]
    tlist.append(row)
star_name=[]
Distance=[]
Mass=[]
Radius=[]
Lum=[]
for i in range(1,len(tlist)):
    star_name.append(tlist[i][1])
    Distance.append(tlist[i][3])
    Mass.append(tlist[i][5])
    Radius.append(tlist[i][6])
    Lum.append(tlist[i][7])
df2=pd.DataFrame(list(zip(star_name,Distance,Mass,Radius,Lum)),columns=["star_name","Distance","Mass","Radius","Lum"])
df2.to_csv("brightstars.csv")