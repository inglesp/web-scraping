# This script searches for a term on StackOverflow and shows the title of the
# first result .

import sys

import bs4
import requests


search_term = sys.argv[1]

rsp = requests.get('http://stackoverflow.com/search?q=' + search_term)
doc = bs4.BeautifulSoup(rsp.text, 'html.parser')

result_links = doc.find_all(class_='result-link')

print('The highest-ranked posts for {} are:'.format(search_term))

for div in result_links:
    print(div.text.strip())
