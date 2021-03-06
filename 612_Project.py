#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 20:37:04 2018
"""


import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
import argparse
import removeduplicates
import FormSubmitter as Form
parser = argparse.ArgumentParser(description='Takes in filters for craigslist search (exclusively for motorcycles and cars)')
parser.add_argument("-m", "--motorcycle", help="Boolean For Motorcycle Search", action="store_true")
parser.add_argument("-c", "--car", help="Boolean For Car Search", action="store_true")
parser.add_argument("-mi", "--miles", help="Miles from zip (default: None)", action="store", default=None)
parser.add_argument("-z", "--zip", help="Zipcode (default: None)", action="store", default=None)
parser.add_argument("-minp", "--min_price", help="Minimum price of the item (default: None)", action="store", default=None)
parser.add_argument("-maxp", "--max_price", help="Maximum price of the item (default: None)", action="store", default=None)
parser.add_argument("-ma", "--make", help="Make of the item (default: None)", action="store", default=None)
parser.add_argument("-mo", "--model", help="Model of the item (default: None)", action="store", default=None)
parser.add_argument("-minen", "--min_eng_disp", help="Minimum engine displacement (default: None)", action="store", default=None)
parser.add_argument("-maxen", "--max_eng_disp", help="Maximum engine displacement (default: None)", action="store", default=None)
parser.add_argument("-miny", "--min_year", help="Minimum model year (default: None)", action="store", default=None)
parser.add_argument("-maxy", "--max_year", help="Maximum model year (default: None)", action="store", default=None)
parser.add_argument("-mino", "--min_odo", help="Minimum odometer (default: None)", action="store", default=None)
parser.add_argument("-maxo", "--max_odo", help="Maximum odometer (default: None)", action="store", default=None)
parser.add_argument("-con", "--condition", help="Condition of the item (Options: new, like new, excellent, good, fair, salvage) (default: None)", action="store", default=None)
parser.add_argument("-f", "--fuel", help="Type of fuel for item (Options: gas, diesel, hybrid, electric, other) (default: None)", action="store", default=None)
parser.add_argument("-col", "--color", help="Color of the item (Options: black, blue, brown, green, grey, orange, purple, red, silver, white, yellow, custom, all) (default: None)", action="store", default=None)
parser.add_argument("-ti", "--title", help="Title status (Options: clean, salvage, rebuilt, parts_only, lien, missing) (default: None)", action="store", default=None)
parser.add_argument("-tr", "--trans", help="Transmission (Options: manual, automatic, other) (default: None)", action="store", default=None)
parser.add_argument("-l", "--location", help="Location of the item (default: None)", action="store", default=None)
results = parser.parse_args()
#for location, do zipcode lookup with city and state ex.(Durham,NH)

#need to make either of these required arguments
#have to type -c or -m
if (results.car == None and results.motorcycle == None) or (results.car and results.motorcycle):
    print('Need to select either -c or -m option')
    quit()
if results.car:
    baseUrl = 'https://boston.craigslist.org/search/cta?sort=rel'
if results.motorcycle:
    baseUrl = 'https://boston.craigslist.org/search/mca?sort=rel'
if results.zip == None:
    print("need a zipcode")
    quit()
    

#print("results: " + str(results))
#declare variables
miles='';postal='';min_price='';max_price='';make='';model=''
min_eng_disp='';max_eng_disp='';min_year='';max_year=''
min_odo='';max_odo='';condition='';fuel='';color=''
title='';trans='';location='';query='';


if results.make:
    make = str(results.make)
    
if results.model:
    model = str(results.model)
    
#query with make and model
if results.make and results.model:
    baseUrl = baseUrl + '&query=' + make + "+" + model
if results.make and results.model == None:
    #print('1')
    baseUrl = baseUrl + '&query=' + make
if results.make == None and results.model:
    #print('2')
    baseUrl = baseUrl + '&query=' + model

if results.miles:
    miles = "&search_distance=" + str(results.miles)
    baseUrl = baseUrl + miles
    
if results.zip:
    postal = "&postal=" + str(results.zip)
    baseUrl = baseUrl + postal
    
if results.min_price:
    min_price = "&min_price=" + str(results.min_price)
    baseUrl = baseUrl + min_price
    
if results.max_price:
    max_price = "&max_price=" + str(results.max_price)
    baseUrl = baseUrl + max_price

if results.min_eng_disp:
    min_eng_disp = "&min_engine_displacement_cc=" + str(results.min_eng_disp)
    baseUrl = baseUrl + min_eng_disp
    
if results.max_eng_disp:
    max_eng_disp = "&max_engine_displacement_cc=" + str(results.max_eng_disp)
    baseUrl = baseUrl + max_eng_disp
    
if results.min_year:
    min_year = "&min_auto_year=" + str(results.min_year)
    baseUrl = baseUrl + min_year
    
if results.max_year:
    max_year = "&max_auto_year=" + str(results.max_year)
    baseUrl = baseUrl + max_year
    
if results.min_odo:
    min_odo = "&min_auto_miles=" + str(results.min_odo)
    baseUrl = baseUrl + min_odo
    
if results.max_odo:
    max_odo = "&max_auto_miles=" + str(results.max_odo)
    baseUrl = baseUrl + max_odo
    
if results.condition:
    condition = "&condition=" + str(results.condition)
    baseUrl = baseUrl + condition
    
if results.fuel:
    fuel = "&auto_fuel_type=" + str(results.fuel)
    baseUrl = baseUrl + fuel
    
if results.color:
    color = "&auto_paint=" + str(results.color)
    baseUrl = baseUrl + color
    
if results.title:
    title = "&auto_title_status=" + str(results.title)
    baseUrl = baseUrl + title
    
if results.trans:
    trans = "&auto_transmission=" + str(results.trans)
    baseUrl = baseUrl + trans
    
if results.location:
    location = "&postal=" + str(results.location)
    baseUrl = baseUrl + location


print(baseUrl)        
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import random
def random_proxy():
    return random.randint(0, len(proxies) - 1)
userAg = UserAgent()
proxies = []
# Retrieve latest proxies
proxies_req = Request('https://www.sslproxies.org/')
proxies_req.add_header('User-Agent', userAg.random)
proxies_doc = urlopen(proxies_req).read().decode('utf8')
soup = BeautifulSoup(proxies_doc, 'html.parser')
proxies_table = soup.find(id='proxylisttable')

# Save proxies in the array
for row in proxies_table.tbody.find_all('tr'):
    proxies.append({'ip' : row.find_all('td')[0].string, 'port' : row.find_all('td')[1].string})

# Choose a random proxy
proxy_index = random_proxy()
proxy = proxies[proxy_index]
for p in proxies:
    req = Request(baseUrl)
    req.set_proxy(proxy['ip'] + ':' + proxy['port'], 'http')
    try:
        test = urlopen(baseUrl)
    except:
        del proxies[proxy_index]
        proxy_index = random_proxy()
        proxy = proxies[proxy_index]

rec = open("initialRecommendations.csv", 'w')
rec.write('date' + "," + 'title' + "," + 'link' + ',' + 'price' + "," + 'year' + ',' + 'Make/Model' + ',' + 'odometer' + ',' 
          + 'Color' + ','+ 'Fuel Type' + ','+ 'VIN' + ','+ 'Title Status' + ','+ 'Car Type' + ','
          + 'Transmission' + ','+ 'Size' + ','+ 'Drive' + ','+ 'Cyclinders' + ',' + 'Condition' + ',' '\n')
response = urlopen(baseUrl)
soup = BeautifulSoup(response, "lxml")
lis = []
counter = 0
for child in soup.find_all("li", {"class" : "result-row"}):
    if counter != 25:
       stri = ""
       title = ""
       link = ""
       date = ""
       price = ""
       title = child.p.a.get_text()
       link = child.p.a.attrs['href']
       date = child.p.time.attrs['datetime']
       try:
           price = child.find("span", {"class" : "result-price"}).get_text()
           if "$" not in price:
               exit
           else:
               price = price.replace("," , "")
               price = price.replace("$", "")
       except:
           price = "N/A"
       stri = date + "," + title + "," + link + "\n"
       req1= Request(baseUrl)
       req1.set_proxy(proxy['ip'] + ':' + proxy['port'], 'http')
       print('proxy set')
       counter = counter + 1
       if counter % 5 == 0:
           proxy_index = random_proxy()
           proxy = proxies[proxy_index]
           print('proxy: ' , proxy)
       if stri not in lis:
           lis.append(stri)
           nextlink = urlopen(link)
           soup2 = BeautifulSoup(nextlink, "lxml")
           listofstrings=[]
           count=0
           for child2 in soup2.find_all("p", {"class" : "attrgroup"}):
               datadict={}
               childlist=[]
               datadict = {'name':"" ,'odometer':"",'paint color':"",'fuel':"",
                           'VIN':'','title status':"",'type':"",'transmission':"",
                           'size':"",'drive':"",'cylinders':"",'condition':""}
               count=count+1
               if count == 2:
                   for children in child2.find_all('span'):
                       listofstrings.append(children.get_text())       
               else:        
                   listofstrings.append(child2.get_text().strip())
                   
                #print(listofstrings)
               datadict['name'] = listofstrings[0]
               #print(datadict)
               
               for data in listofstrings:
                   keyvalue = data.split(":")
                   try:
                       keyvalue[1]=keyvalue[1].strip()
                   except IndexError:
                       pass
                   #print(keyvalue)
                   try:
                       datadict[keyvalue[0]]=keyvalue[1]
                   except IndexError:
                       pass
               for k in datadict:
                   if datadict[k] == '':
                       datadict[k] = 'N/A'
               print("data: " , datadict)
               #print(listofstrings)
               #print(child2.get_text())     
               #search description for other form inputs?
           try:
               stri = (str(date) + "," + str(title).replace(',','') + "," + str(link) + "," + str(price) + "," + str(datadict['name'][0:4]) + "," + str(datadict['name'][5:]) + "," + str(datadict['odometer']) + "," 
               + str(datadict['paint color']) + ","+ str(datadict['fuel']) + ","+ str(datadict['VIN']) + ","+ str(datadict['title status']) + "," 
               + str(datadict['type']) + ","+ str(datadict['transmission']) + ","+ str(datadict['size']) + ","+ str(datadict['drive']) + ","
               + str(datadict['cylinders']) + ","+ str(datadict['condition']) + "\n")
               rec.write(stri)
           except:
               stri = (str(date) + "," + "Bad Encoding!" + "," + str(link) + "," + str(price) + "," + str(datadict['name'][0:4]) + "," + str(datadict['name'][5:]) + "," + str(datadict['odometer']) + "," 
               + str(datadict['paint color']) + ","+ str(datadict['fuel']) + ","+ str(datadict['VIN']) + ","+ str(datadict['title status']) + "," 
               + str(datadict['type']) + ","+ str(datadict['transmission']) + ","+ str(datadict['size']) + ","+ str(datadict['drive']) + ","
               + str(datadict['cylinders']) + ","+ str(datadict['condition']) + "\n")
               rec.write(stri)
       else:
           print('pass')
           pass
    else:
        break
rec.close()

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
def visualize():    
    noDup = open('NoDuplicates.csv' , 'r',encoding='latin-1')
    fig = plt.figure()
    ax = fig.add_subplot(111)
    priceList = []
    firstRow = True
    names = []
    recPriceList = []
    for row in noDup:
        if firstRow == True:
            firstRow = False
            pass
        else:
            token = row.split(',')
            price = token[3]
            name = token[4] + token[5] + token[6]
            recPrices = token[18]
            if recPrices == "Not Enough Pricing Data" or recPrices == "Bad Data":
                recPrices = 0
                recPriceList.append(float(recPrices))
            else:
                recPriceList.append(float(recPrices))
            names.append(name)
            if price == "N/A":
                pass
            else:
                price = price.replace("$", "")
                print(price)
                priceList.append(float(price))
    print(priceList)
    print(names)
    print(recPriceList)
    ind = np.arange(len(priceList))
    width = 0.35
    rects = ax.bar(ind, priceList, width, color='red')
    rects1 = ax.bar(ind+width, recPriceList, width, color='blue')
    ax.set_xlim(-width,len(ind)+width)
    ax.set_xticks(ind+width)
    xtickNames = ax.set_xticklabels(names)
    ax.legend((rects[0],rects1[0]),('Craigslist Price','Recommended Price'))
    ax.set_ylabel('Price')
    ax.set_xlabel('Titles')
    ax.set_title('Prices of recommendations')
    plt.setp(xtickNames, rotation=45, fontsize=8)
    plt.tight_layout()
    plt.show()
    
#remove duplicates
fileName = results.make + "_" + results.model + "_" + results.zip
removeduplicates.removedupe(results.zip)

#visulaize it
visualize()

#move files with bash
import subprocess
subprocess.check_call(["./move.sh", fileName])
#subprocess.call(['mkdir' fileName,mv NoDuplicates.csv fileName,mv initialRecommendations.csv fileName])






    
