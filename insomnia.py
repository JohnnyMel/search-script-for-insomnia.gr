#!/usr/local/bin/python
# encoding=utf8  
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

import bs4
import urllib2
import re
import os

import os.path as pt
import sys
from time import sleep
import requests
import argparse


def find_urls(page_url, search, rmFilter, priceRange):
    response = requests.get(page_url, verify=True)
    soup = bs4.BeautifulSoup(response.text,"html.parser") 

    srch = search.split()
    allMatched = len(srch)
    
    pRange = ''
    
    if priceRange is not '':
        pRange = priceRange.split("-")
            
    tables = soup.findChildren('table')
    table = tables[0]
        
    rows = table.findChildren('tr')
    count = 0
    
    for row in rows:
        columns = row.findChildren('td')
        for column in columns:
            link = column.find('a')
            price = row.find_all("td", class_="short")
            if link is not None:
                title = link.get("title")
                if title is not None:
                    count = 0;
                    for s in srch:
                        if s.lower() in title.lower():
                            count += 1
                            if count == allMatched:
                                if rmFilter is '!':
                                    if '€' not in price[2].text:
                                        break
                                
                                if len(pRange) > 1:
                                    if '€' not in price[2].text:
                                        break
                                    plainPrice = price[2].text.split("€")
                                    if int(plainPrice[1]) < int(pRange[0]) or int(plainPrice[1]) > int(pRange[1]): 
                                        break
                                
                                print title
                                print price[2].text
                                print link.get("href") + "\n"
            if count == allMatched:
                break
                
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("url", type=str,help="το URL link της σελίδας με τις αγγελίες π.χ.το URL των κινητών")
    parser.add_argument("query", type=str,help='τα κριτήρια αναζήτησης π.χ. "smartphone model" (μαζί με τα εισαγωγικά)')
    parser.add_argument("pages", type=int,help="σε πόσες σελίδες θα ψάξει")
    
    parser.add_argument("-f", "--filter", action="store_true", help="αφαιρεί τις αγγελίες που δεν έχουν τιμή")
    parser.add_argument("-r", "--range", type=str, help="εύρος τιμής π.χ. 50-200")
    
    args = parser.parse_args()
    
    sum = 0
    rmFilter = ' '
    priceRange = ''
    
    if args.filter:
        rmFilter = '!'
    
    if args.range is not None:
        priceRange = args.range
    
    for i in range(int(args.pages)):
        print "page " + str(i+1) + " =====================================================\n" 
        find_urls(args.url + "?st=" + str(sum), args.query, rmFilter, priceRange)
        sum += 15
    

main()