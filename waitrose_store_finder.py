# This script finds the latitude and longitude of all stores listed on the
# Waitrose website.

import bs4
import requests


def clean_branch_name(branch_name):
    for prefix in [
        'Welcome to Waitrose',
        'Waitrose at',
        'Waitrose',
        'Little Waitrose at',
        'Little Waitrose',
    ]:
        if branch_name.lower().startswith(prefix.lower()):
            branch_name = branch_name[len(prefix):]

    if branch_name.lower().endswith('waitrose'):
        branch_name = branch_name[:-len('waitrose')]

    branch_name = branch_name.strip(' -')

    if branch_name.lower().endswith('waitrose.com'):
        branch_name = branch_name[:-len('waitrose.com')]

    branch_name = branch_name.strip(' -')

    if branch_name.lower().endswith('branch finder'):
        branch_name = branch_name[:-len('branch finder')]

    branch_name = branch_name.strip(' -')

    return branch_name


def scrape():
    rsp = requests.get('http://www.waitrose.com/content/waitrose/en/bf_home/bf.html')
    doc = bs4.BeautifulSoup(rsp.text, 'html.parser')
    select = doc.find('select', id='global-form-select-branch')

    for option in select.find_all('option'):
        value = option['value']
        if value:
            rsp = requests.get('http://www.waitrose.com/content/waitrose/en/bf_home/bf/{}.html'.format(value))
            doc = bs4.BeautifulSoup(rsp.text, 'html.parser')

            branch_name = clean_branch_name(doc.find(id='current-breadcrumb').text.strip())
            if branch_name == 'errors':
                continue

            map_link = doc.find(class_='load-branch-map')
            print('{}\t{}\t{}'.format(branch_name, map_link['data-lat'], map_link['data-long']))


if __name__ == '__main__':
    scrape()
