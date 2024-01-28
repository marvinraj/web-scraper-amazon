""" the purpose of this file is to continuosly enhance
the program/scraper """

import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.in/s?k=keychron+keyboard&crid=13X0BQCSF8P9V&sprefix=keychron+keyboard%2Caps%2C254&ref=nb_sb_noss_1"
HEADERS = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}

page = requests.get(URL, headers=HEADERS)

# Soup object that contains all the data from the URL
soup = BeautifulSoup(page.content, "html.parser") 

links = soup.find_all("a", attrs={'class': 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})

link_1 = links[1].get('href')
product_link = "https://www.amazon.in/" + link_1


new_page = requests.get(product_link, headers=HEADERS)

# Soup object that contains all the data from the URL
new_soup = BeautifulSoup(new_page.content, "html.parser") 

# obtain title of the product
title = new_soup.find("span", {"id":"productTitle"})
title = title.get_text(strip=True)
print(title)

# obtain price of the product
price = new_soup.find("span", attrs={"class":"a-price aok-align-center reinventPricePriceToPayMargin priceToPay"}).find("span", attrs={"class":"a-offscreen"}).text

print(price)