import csv
from types import SimpleNamespace

# from pprint import pprint
import requests
# import os
from bs4 import BeautifulSoup
import time # slow down requests
from requests_cache import CachedSession
from urllib.parse import quote

# loading from file
# file_path = "UN_countries_full.html"
# if os.path.exists(file_path):
#     print(f"The file '{file_path}' exists.")
# else:
#     print(f"The file '{file_path}' does not exist.")
#
# with open('UN_countries_full.html', 'r') as file:
#     html_doc = file.read()

USE_CACHE = True

# setup cache
if USE_CACHE:
    session = CachedSession('scraper_cache',
                            backend='sqlite',
                            # expire_after=60 * 60 * 24 * 30, # 30 days
                            expire_after=0,
                            refresh=False,
                            allow_expired=False,
                            allowable_codes=(200,),
                            stale_if_error=True,
                            cache_control=False)  # ignore Cache-Control headers

else:
    import types
    session = types.SimpleNamespace(get=requests.get())

# loading from web
URL = "https://en.wikipedia.org/wiki/Member_states_of_the_United_Nations"
HEADERS = {'User-Agent': 'Mozilla/5.0'}
# def get_url(url):
#     if not USE_CACHE:
#         time.sleep(0.5)
#     response = session.get(url, headers=HEADERS)
#     response.raise_for_status()
#     return response.text

def get_url(url):
    response = session.get(url, headers=HEADERS)
    # for debug
    print(f"Passed URL: {url}")
    print(f"Final URL : {response.url}")
    # print(f"GET {url} -> {response.url} [from_cache={getattr(response, 'from_cache', False)}]")

    # Only check this if using cache
    if USE_CACHE and hasattr(response, 'from_cache'):
        if response.from_cache:
            print(f"[CACHE]   : {url}")
        else:
            print(f"[FETCH]   : {url}")

    if not USE_CACHE:
        time.sleep(0.5)

    response.raise_for_status()
    return response.text

html_doc = get_url(URL)
if USE_CACHE:
    print(session.cache)
    print('Cached URLS:')
    print('\n'.join(session.cache.urls()))


soup = BeautifulSoup(html_doc, "html.parser")
# print(soup.prettify())

table = soup.find('table', class_='wikitable')
if not table:
    raise ValueError("Could not find the target table. Page structure may have changed.")

rows = table.find_all('tr')


# generator
def parse_country_rows(rows):
    for i, row in enumerate(rows):
        if i == 0:
            yield "Country Name", "Date Joined"
            continue
        th = row.th
        td = row.td
        name_link = th.a
        yield name_link['title'], td.span.text

def parse_country_geo(country):
    try:
        url = f"https://en.wikipedia.org/wiki/{quote(country)}"
        # url = "https://en.wikipedia.org/wiki/" + country.replace(' ', '_')
        html_doc = get_url(url)
        soup = BeautifulSoup(html_doc, "html.parser")

        coords = soup.find_all('span', id='coordinates')
        if not coords:
            return "N/A","N/A"

        geo = coords[0].find_all('span', class_='geo-default')
        # pprint(geo)
        if geo and geo[0].find('span', class_='geo-dms'):
            return (
                geo[0].find('span', class_='longitude').text,
                geo[0].find('span', class_='latitude').text
            )
        elif geo and geo[0].find('span', class_='geo-dec'):
            pos = geo[0].find('span', class_='geo-dec').text
            return tuple(pos.split(' '))
        else:
            return "N/A","N/A"

    except Exception as e:
        print(f"[ERROR] {country}: {e=} ")
        return "N/A", "N/A"

def parse_country_rows_with_geo(rows):
    for i, row in enumerate(rows):
        # if i == 20:
        #     break
        if i == 0:
            yield "Country Name", "Date Joined", "Longitude", "Latitude"
            continue
        th = row.th
        td = row.td
        name_link = th.a
        country_name = name_link['title']
        date_joined = td.span.text
        (longitude, latitude) = parse_country_geo(country_name)
        print(country_name, longitude, latitude)
        yield country_name, date_joined, longitude, latitude

country_date = []
with open('countries_name.txt', 'w', encoding='utf-8') as output:
    for name, date in parse_country_rows(rows):
        country_date.append([name, date])
        output.write(f"{name}\t{date}\n")

with open('countries_name.csv', 'w', encoding='utf-8', newline='') as output:
    writer = csv.writer(output)
    # use generator as iterable
    writer.writerows(country_date)
    # or loop
    # for name, date in country_date
    #     writer.writerow([name, date])

country_date_geo = []
with open('countries_name_with_geo.txt', 'w', encoding='utf-8') as output:
    for name, date, longitude, latitude in parse_country_rows_with_geo(rows):
        country_date_geo.append([name, date, longitude, latitude])
        output.write(f"{name}\t{date}\t{longitude}\t{latitude}\n")

with open('countries_name_geo.csv', 'w', encoding='utf-8', newline='') as output:
    writer = csv.writer(output)
    # use generator as iterable
    writer.writerows(country_date_geo)
