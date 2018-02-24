from src.champions.champions import Champions
from src.summoner.summoner import Summoner
from utils.json_to_dict import to_dict


def main(config):
    summoner_name = input('Summoner Name: ')
    summoner = Summoner(summoner_name, config['api_secret_key'])
    champions = Champions(config['api_secret_key'])

    print('{}\n{}\n{}\n{}\n{}\n{}'.format(summoner.name,
                                          summoner.account_id,
                                          summoner.summoner_id,
                                          summoner.roles,
                                          summoner.champions_mastery,
                                          champions.get_all_champions_info()))


if __name__ == '__main__':
    config = to_dict('config/riot_dev_api_key.json')
    main(config)
