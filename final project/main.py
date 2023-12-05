#this file was created by Jackson Koberlein on 11/27/23


#import browser from web
import webbrowser
#import libraries 
import bs4
import requests
import selenium 


''' 
--flightaware scaper--

goals
-program can output flight information from flight aware database (https://www.flightaware.com/live/)
-program can show when flights are landing at a particular airport (https://www.flightaware.com/live/airport/KSFO)
-program is able to change between different airports
-program can make popup when flight lands at selected airport
    -popup with graphic of the plane type that landed

https://github.com/shivasiddharth/Flightaware-Parser

https://automatetheboringstuff.com/2e/chapter12/

'''

#open web site 
#webbrowser.open('https://www.flightaware.com/live/airport/KSFO')

#get info from website
html_text = requests.get('https://www.flightaware.com/live/airport/KSFO').text

class scraper: 
    def __init__(self): 
        self.urlbase = 'https://www.flightaware.com/live/airport/KSFO'