import json
import os

import urllib.request as ur

CLIENT_ID = os.getenv('UNTAPPD_CLIENT_ID')
CLIENT_SEC = os.getenv('UNTAPPD_CLIENT_SECRET')
URL = 'https://api.untappd.com'
BEER_SEARCH_URL = URL+'/v4/search/beer'

DEBUG = True
RUN_DEBUG = False
if __name__ == '__main__':
    RUN_DEBUG = True
DONT_REQUEST = False


def search_beer(beer_name):
    beer_name_url = ur.quote(beer_name)
    if DEBUG:
        print(beer_name_url)
    request = (
            BEER_SEARCH_URL + '?client_id=' + CLIENT_ID +
            '&client_secret='+CLIENT_SEC+'&q=' + beer_name_url
    )
    if DEBUG:
        print(request)
    if DONT_REQUEST:
        return None
    response = ur.urlopen(request)
    if response.status != 200:
        print('Have {} response status'.format(response.status))
        return None

    data = json.load(response)

    if data['meta'] is not None and data['meta']['code'] is not None:
        if data['meta']['code'] != 200:
            return None
    else:
        return None

    try:
        beers = data['response']['beers']
        if beers['count'] == 0:
            return None
        beer_info = beers['items'][0]
        if DEBUG:
            print('some beer found: ', beer_info)
        beer = beer_info['beer']
        brewery = beer_info['brewery']
        res = {}
        res['name'] = beer['beer_name']
        res['abv'] = beer['beer_abv']
        res['ibu'] = beer['beer_ibu']
        res['style'] = beer['beer_style']
        res['brewery'] = brewery['brewery_name']
        res['country'] = brewery['country_name']
        return res
    except IndexError as er:
        print('Error requesting beer {}, error: {}'.format(beer_name, er))
        print('request = ', request)
        return None
    except Exception as er:
        print('Error requesting beer {}, error: {}'.format(beer_name, er))
        print('request = ', request)
        return None

if RUN_DEBUG:
    searchname = 'rouge hazelnut'
    res = search_beer(searchname)
    print('')
    print('')
    print(res)
