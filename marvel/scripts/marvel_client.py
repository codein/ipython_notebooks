from datetime import datetime
import json
import logging
import md5
import requests

import settings


class MarvelClient(object):
    """
    MarvelClient is a HTTP client to fetch data from Marvel's API
    http://gateway.marvel.com:80/v1/public
    """
    def __init__(self, public_key, private_key):
        self.public_key = public_key
        self.private_key = private_key
        self.base_url = 'http://gateway.marvel.com:80/v1/public'
        self.set_logger()

    def set_logger(self):
        # create logger
        logger = logging.getLogger('MarvelClient')
        logger.setLevel(logging.DEBUG)
        # create console handler and set level to debug
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        # create formatter
        formatter = logging.Formatter('%(asctime)s - %(filename)s:%(lineno)d - %(levelname)s - %(message)s')
        # add formatter to ch
        ch.setFormatter(formatter)
        # add ch to logger
        logger.addHandler(ch)
        self.logger = logger

    def get_current_hash(self):
        """
        Ref http://developer.marvel.com/documentation/authorization
        """
        ts = datetime.now().isoformat()

        m = md5.new()
        m.update(ts)
        m.update(self.private_key)
        m.update(self.public_key)
        hash_digest = m.hexdigest()

        return {
            'ts': ts,
            'hash': hash_digest
        }


    def fetch_characters(self, offset=0):
        """
        fetches and returns a dict representing the character.
        offset: the offset at which the character exists
        """
        url = '%s/%s' % (self.base_url, 'characters')
        limit = 1
        params = {
            'apikey': self.public_key,
            'orderBy': 'name',
            'limit': limit,
            'offset': offset
        }

        params.update(self.get_current_hash())
        response = requests.get(url, params=params)
        query_result = json.loads(response.text)
        return query_result['data']['results'][0]

    def save_characters(self, start=0, stop=1):
        """
        fetches and saves characters to disk.
        start/stop : the offset at which to start/stop fetching characters
        """
        for idx in range(start, stop):
            character = self.fetch_characters(idx)
            character_name =  character['name'].strip().replace('/', '-')
            character_file = open('../character/%s.json' % character_name, 'w+')
            character_file.write(json.dumps(character))
            character_file.close()
            self.logger.info('Saved character %s at idx %d', character_name, idx)

if __name__ == "__main__":
    marvel_client = MarvelClient(settings.public_key, settings.private_key)
    marvel_client.save_characters(475,1402)
