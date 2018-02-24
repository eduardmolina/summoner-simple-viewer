import requests
import json


class Summoner(object):
    _summoner_api_uri = 'https://br1.api.riotgames.com/lol/summoner/v3/summoners/by-name/'
    _match_api_uri = 'https://br1.api.riotgames.com/lol/match/v3/matchlists/by-account/'
    _champions_m_api_uri = 'https://br1.api.riotgames.com/lol/champion-mastery/v3/champion-masteries/by-summoner/'

    def __init__(self, name, api_key):
        self.name = name
        self._summoner_props = self._get_summoner(Summoner._summoner_api_uri, api_key)
        self.account_id = self._summoner_props['accountId']
        self.summoner_id = self._summoner_props['id']
        self.roles = self._get_roles(Summoner._match_api_uri, api_key)
        self.champions_mastery = self._get_champions_mastery(Summoner._champions_m_api_uri, api_key)

    def _get_summoner(self, summoner_api_uri, api_key):
        try:
            response = json.loads(requests.get('{}{}?api_key={}'.format(summoner_api_uri, self.name, api_key)).text)
        except Exception as error:
            print(error)
            raise
        return response

    def _get_roles(self, match_api_uri, api_key):
        try:
            response = json.loads(requests.get('{}{}?api_key={}'.format(match_api_uri, self.account_id, api_key)).text)
        except Exception as error:
            print(error)
            raise
        return response

    def _get_champions_mastery(self, champions_mastery_api_uri, api_key):
        try:
            response = json.loads(
                requests.get('{}{}?api_key={}'.format(champions_mastery_api_uri, self.summoner_id, api_key)).text)
        except Exception as error:
            print(error)
            raise
        return response
