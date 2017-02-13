# This script uses the Google Maps Geocoding API to find the latitude and
# longitude of a given address.

import sys

import requests

address = sys.argv[1]

url = 'http://maps.googleapis.com/maps/api/geocode/json'
params = {
    'address': address,
    'sensor': 'false',
}

response = requests.get(url, params=params)
data = response.json()

if data['status'] == 'OK':
    if len(data['results']) > 1:
        print('Multiple results returned for {}'.format(address))
    else:
        result = data['results'][0]
        location = result['geometry']['location']
        print('latitude:', location['lat'])
        print('longitude:', location['lng'])
elif data['status'] == 'ZERO_RESULTS':
    print('No results returned for {}').format(address)
else:
    message = '{} ({})'.format(data['status'], data.get('error_message', 'no specific error'))
    print(message)

