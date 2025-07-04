import csv
from pprint import pprint
import requests
from bs4 import BeautifulSoup

# loading from web
URL = "https://en.wikipedia.org/wiki/Albania"
response = requests.get(URL)
response.raise_for_status()
html_doc = response.text


soup = BeautifulSoup(html_doc, "html.parser")
# print(soup.prettify())

coords = soup.find_all('span', id='coordinates')
print(len(coords))
geo = coords[0].find_all('span', class_='geo-default')
pprint(geo)
longitude = geo[0].find('span', class_='longitude')
latitude = geo[0].find('span', class_='latitude')
print(longitude.text)
print(latitude.text)
