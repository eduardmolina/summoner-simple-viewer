import requests
import json


class Champions(object):
    _champions_i_uri = 'https://br1.api.riotgames.com/lol/static-data/v3/champions?locale=pt_BR&dataById=false&api_key='

    def __init__(self, api_key):
        self.api_key = api_key

    def get_all_champions_info(self):
        try:
            response = json.loads(requests.get('{}{}'.format(Champions._champions_i_uri, self.api_key)).text)
        except Exception:
            raise ValueError('[*] Get Champions Info Error')
        return response
