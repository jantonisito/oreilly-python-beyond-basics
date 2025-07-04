"""
Print the text of the two buttons on the Google homepage.

Documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
"""
from bs4 import BeautifulSoup

with open('data/google.html', 'r') as file:
    html_doc = file.read()

soup = BeautifulSoup(html_doc, 'html.parser')
#print(soup.prettify())

# Find all submit buttons
# easy way to do it is to right clock on button on web page and
# select 'Inspect element'
#buttons = soup.find_all("input", {"type": "submit"})
buttons = soup.find_all(lambda tag: tag.name in ['button', 'input'] and tag.get('type') == 'submit')

for btn in buttons:
    print(f"Name: {btn.get('name')}, Value: {btn.get('value')}")