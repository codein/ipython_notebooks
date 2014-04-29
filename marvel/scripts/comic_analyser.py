import glob
import json
import random

from collections import defaultdict

from knowledge import top_characters

def sort(character):
    return top_characters.index(character['name'])

def parse_comics_files(directory):
    character_map = defaultdict(set)
    count = 0
    for filename in glob.iglob('%s/*.json' % directory):
        count += 1
        print count
        # sampling
        # if count > 1000:
            # return character_map
        comic_file = open(filename)
        comic = json.load(comic_file)
        characters_record = comic.get('characters', {})
        if random.choice(range(30)) == 1 and characters_record and characters_record.get('available', 0) > 1:
            characters = characters_record.get('items', [])
            character_names = [character['name'] for character in characters if character['name'] in top_characters]

            for name in character_names:
                character_map[name].update(character_names)

    return character_map

character_map = parse_comics_files('../comics')
characters = []
for character,co_characters in character_map.iteritems():
    co_characters.remove(character)
    character = {
        'name':character,
        'imports': list(co_characters),
    }
    characters.append(character)

characters = sorted(characters, key=sort)

flare_file = open('../flare-characters.json', 'w+')
json.dump(characters, flare_file
          # sort_keys=True,
          # indent=4,
          # separators=(',', ': ')
         )





