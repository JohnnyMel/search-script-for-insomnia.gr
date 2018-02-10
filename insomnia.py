#!/usr/local/bin/python
# encoding=utf8  
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

import bs4
import urllib2
import os

import sys
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
            
    lists = soup.findChildren('li', class_="ipsDataItem   ")
    
    count = 0
    
    for list in lists:
        link = list.find('a', class_="ipsTruncate ipsTruncate_line")
        price = list.find("strong", class_="ipsType_normal")
        if link is not None:
            title = link.text
            if price is not None:
                price = price.text
            if title is not None:
                count = 0;
                for s in srch:
                    if s.lower() in title.lower():
                        count += 1
                        if count == allMatched:
                            if rmFilter is '!':
                                if price is None:
                                    break
                                
                            if len(pRange) > 1:
                                if price is None:
                                    break
                                plainPrice = price.split("€")
                                plainPrice = plainPrice[0]
                                plainPrice = plainPrice.replace(',','.')
                                if float(plainPrice) < float(pRange[0]) or float(plainPrice) > float(pRange[1]): 
                                    break
                                
                            print title
                            print price
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
    
    rmFilter = ' '
    priceRange = ''
    
    if args.filter:
        rmFilter = '!'
    
    if args.range is not None:
        priceRange = args.range
    
    for i in range(int(args.pages)):
        print "page " + str(i+1) + " =====================================================\n" 
        find_urls(args.url + "?page=" + str(i+1), args.query, rmFilter, priceRange)
        
    

main()