# This script extracts a list of Six Nations champions from Wikipedia.

import bs4
import requests

rsp = requests.get('https://en.wikipedia.org/wiki/Six_Nations_Championship')
doc = bs4.BeautifulSoup(rsp.text, 'html.parser')

span = doc.find('span', class_='mw-headline', text='Six Nations (2000–present)')
h3 = span.parent

for element in h3.next_siblings:
    if isinstance(element, bs4.element.Tag) and element.name == 'table':
        table = element
        break

trs = table.find_all('tr')

tr = trs[1]

ths = tr.find_all('th')
assert ths[0].text.strip() == 'Year'
assert ths[1].text.strip() == 'Champions'

for tr in trs[2:]:
    tds = tr.find_all('td')
    year = tds[0].text.strip()
    champion = tds[1].text.strip()
    
    if champion != '–':
        print('In {}, the champions were {}'.format(year, champion))
