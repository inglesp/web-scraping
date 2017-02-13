# This script searches Spotify for albums matching a given search term.

import sys

import requests

search_term = sys.argv[1]

url = 'https://api.spotify.com/v1/search?type=album&q=' + search_term

while True:
    rsp = requests.get(url)
    data = rsp.json()
    items = data['albums']['items']
    for item in items:
        title = item['name']
        artist_names = '; '.join(artist['name'] for artist in item['artists'])
        print('{} ({})'.format(title, artist_names))

    url = data['albums']['next']
    if url is None:
        break
