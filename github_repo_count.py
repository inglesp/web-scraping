# This script tells you how many public repositories you have on GitHub, and
# then uses your password to log in and find out how many repositories you have
# in total.

from getpass import getpass
import sys

import bs4
import requests


username = sys.argv[1]
password = getpass('Please enter your GitHub password')

user_url = 'https://github.com/{}/'.format(username)
login_url = 'https://github.com/session'

session = requests.Session()

rsp = session.get(user_url)
doc = bs4.BeautifulSoup(rsp.text, 'html.parser')

a = doc.find('a', href='/{}?tab=repositories'.format(username))
span = a.find('span', class_='counter')
num_repos_public = int(span.text.strip())
print('You have {} public repos'.format(num_repos_public))

rsp = session.get('https://github.com/login')
doc = bs4.BeautifulSoup(rsp.text, 'html.parser')

input_ = doc.find('input', attrs={'name': 'authenticity_token'})
authenticity_token = input_['value']

data = {
    'commit': 'Sign in',
    'login': username,
    'password': password,
    'authenticity_token': authenticity_token,
    'utf8': '✓',
}

rsp = session.post(login_url, data=data)

rsp = session.get(user_url)
doc = bs4.BeautifulSoup(rsp.text, 'html.parser')

a = doc.find('a', href='/{}?tab=repositories'.format(username))
span = a.find('span', class_='counter')
num_repos_total = int(span.text.strip())
print('You have {} repos in total'.format(num_repos_total))
