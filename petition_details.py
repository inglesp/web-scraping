# This script looks up a petition on UK Parliament Petition website.

import sys

import bs4
import requests


petition_id = sys.argv[1]

rsp = requests.get('https://petition.parliament.uk/petitions/' + petition_id)
doc = bs4.BeautifulSoup(rsp.text, 'html.parser')

h1 = doc.find('h1')

if h1.text == 'This petition is gathering support':
    print('This petition is gathering support')
    exit()

title = h1.text.strip().splitlines()[1].strip()
num_signatures = doc.find('p', class_='signature-count-number').find('span', class_='count').text.strip()

print(title)
print(num_signatures, 'signatures')
