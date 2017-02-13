# The script retrieves all planning applications in Stroud District where a
# decision has been made in the last week, and summarizes the decisions.

from collections import Counter

import bs4
import requests

decision_counts = Counter()

url = 'https://www.stroud.gov.uk/apps/planning'

session = requests.Session()

rsp = session.get(url)
doc = bs4.BeautifulSoup(rsp.text, 'html.parser')

form = doc.find(id='form1')
inputs = form.find_all('input')

data = {}

for inp in inputs:
    key = inp.attrs['name']
    value = inp.attrs.get('value', '')
    data[key] = value

data['__EVENTTARGET'] = 'ctl00$MainContent$sevenDaysLinkButton'
data['__EVENTARGUMENT'] = ''

rsp = session.post(url, data=data)

doc = bs4.BeautifulSoup(rsp.text, 'html.parser')

table = doc.find('table', class_='planningTable')
tbody = table.find('tbody')

for element in tbody.children:
    if element.name == 'tr':
        tds = element.find_all('td')
        status = tds[4].text.strip()
        decision_counts[status] += 1

print('Here is a summary of the planning decisions made in the last seven days:')

for status, count in decision_counts.items():
    print(status, count)
