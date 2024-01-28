""" this scraper extracts data (product name and price) from a 
single dynamic page """

import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.in/dp/B07YDGWWPL"
HEADERS = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}

page = requests.get(URL, headers=HEADERS)

# Soup object that contains all the data from the URL
soup = BeautifulSoup(page.content, "html.parser") 
# print(soup) --> view data
# print(page.status_code) --> view status code, 200 if ok

# obtain title of the product
title = soup.find("span", {"id":"productTitle"})
title = title.get_text(strip=True)
print(title)

# obtain price of the product
price = soup.find("span", {"class":"a-price"})
price = price.get_text(strip=True)
print(price)