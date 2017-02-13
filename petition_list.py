# This script lists all petitions on the UK Parliament Petition website that
# have more than 100,000 signatures.

import bs4
import requests


url = 'https://petition.parliament.uk/petitions'

complete = False

while True:
    rsp = requests.get(url)
    doc = bs4.BeautifulSoup(rsp.text, 'html.parser')

    petition_items = doc.find_all('li', class_='petition-item')

    for item in petition_items:
        title = item.find('h3').text.strip()
        num_signatures = int(item.find('span', class_='count')['data-count'])

        if num_signatures < 100000:
            complete = True
            break

        print(title, num_signatures)

    if complete:
        break

    next_link = doc.find('a', class_='next')
    url = 'https://petition.parliament.uk' + next_link['href']
