import requests
from bs4 import BeautifulSoup
url = "https://www.newegg.com/p/23M-0003-01XR6"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
item_name = soup.find("h1",{"class": "product-title"}).text
item_price = soup.find("li", {"class": "price-current"}).text
print('Item Name: ',item_name,'\nItem Price: ',item_price)
