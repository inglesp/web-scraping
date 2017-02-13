# This script finds all headlines on the BBC News homepage that match a given
# string.

import sys

import bs4
import requests

search_term = sys.argv[1]

rsp = requests.get('http://www.bbc.co.uk/news')
doc = bs4.BeautifulSoup(rsp.text, 'html.parser')

num_found = 0

for h3 in doc.find_all('h3'):
    headline = h3.text.strip()
    if search_term.lower() in headline.lower():
        print(headline)
        num_found += 1

print('Found {} headline(s) matching "{}"'.format(num_found, search_term))
