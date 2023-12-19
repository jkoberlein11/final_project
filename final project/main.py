#this file was created by Jackson Koberlein on 11/27/23


#import browser from web
import webbrowser
#import libraries 
import bs4
from bs4 import BeautifulSoup
import requests
import selenium 
import time

''' 
--flightaware scaper--

goals
-program can output flight information from flight aware database (https://www.flightaware.com/live/)
-program can show when flights are landing at a particular airport (https://www.flightaware.com/live/airport/KSFO)
-program is able to change between different airports
-program can make popup when flight lands at selected airport

https://github.com/shivasiddharth/Flightaware-Parser

https://automatetheboringstuff.com/2e/chapter12/

'''

#open web site 
#webbrowser.open('https://www.flightaware.com/live/airport/KSFO')


#pull website
html_text = requests.get('https://www.flightaware.com/live/airport/KSFO').text

#initiate scraper
soup = BeautifulSoup(html_text, 'lxml')

'''#find div elements 
divelems = soup.select('div')
pelems = soup.select('p')
divElem = soup.select('div')[0]'''
#find information in source code
arrivals= soup.find('tr', class_= 'smallrow1').text.replace('','')
#print information.
print(f"{arrivals} \n")


#pull div element from website code (smallrow1)
#divFind = soup.find('div', {'class': 'smallrow1'})





