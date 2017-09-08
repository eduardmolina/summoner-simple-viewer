"""
Summoner Viewer

Usage: app.py <summoner_name>

IMPORTANT:
    <summoner_name> without space, example "Summoner 123" => "Summoner123"

Options:
    -h  --help
"""

from urllib import request
from data.champions_data import champions_data
from docopt import docopt
from utils.json_to_dict import to_dict
import json

SUMMONER_URL = to_dict('config/summoner_viewer_config.json')['summoner_url']
CHAMPIONS_INFO_URL = to_dict(
    'config/summoner_viewer_config.json')['champions_info_url']
CHAMPIONS_MASTERY_URL = to_dict(
    'config/summoner_viewer_config.json')['champions_mastery_url']
API_SECRET_KEY = to_dict(
    'config/summoner_viewer_config.json')['api_secret_key']


def get_summoner(summoner_name):
    try:
        response = request.urlopen('{}{}?api_key={}'.format(
            SUMMONER_URL, summoner_name, API_SECRET_KEY)).read()
    except Exception as warning:
        print(warning)
    finally:
        return json.loads(response)


def get_champions_mastery(summoner_id):
    try:
        response = request.urlopen('{}{}?api_key={}'.format(
            CHAMPIONS_MASTERY_URL, summoner_id, API_SECRET_KEY)).read()
    except Exception as warning:
        print(warning)
    finally:
        return json.loads(response)


'''
def get_champions_info():
    try:
        response = request.urlopen(
            '{}{}'.format(CHAMPIONS_INFO_URL, API_SECRET_KEY)).read()
    except Exception as warning:
        print(warning)
    finally:
        return json.loads(response)
'''


def get_high_score_champions(champions):
    high_score_champions = list()
    for i in range(10):
        high_score_champions.append(champions[i])
    return high_score_champions


def get_champions_name(high_score_champions, champions_data):
    try:
        for champions in high_score_champions:
            for key, value in champions_data.items():
                if champions['championId'] == value['id']:
                    champions['championName'] = value['name']
    except Exception as warning:
        print(warning)
    finally:
        return high_score_champions


def print_in_format(champions):
    print('\n => Highest Score Champions:\n')
    for champion in champions:
        if(champion.get('championName')):
            print('\t{} - {} points'.format(
                champion['championName'], champion['championPoints']))
        else:
            print('ID: {} not found!'.format(champion['championId']))


if __name__ == '__main__':
    args = docopt(__doc__)
    summoner_name = args['<summoner_name>']
    summoner_dict = get_summoner(summoner_name)
    champions = get_champions_mastery(summoner_dict['id'])
    champions_info = champions_data['data']
    high_score_champions = get_champions_name(
        get_high_score_champions(champions), champions_info)
    print_in_format(high_score_champions)
