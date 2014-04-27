import glob
import json

from xlrd import open_workbook
from xlutils.display import quoted_sheet_name
from xlutils.display import cell_display
from xlwt import Workbook

def parse_character_files(directory):
    characters = []
    for filename in glob.iglob('%s/*.json' % directory):
        character_file = open(filename)
        character = json.load(character_file)
        print character['name']
        characters.append({'comics': character['comics']['available'],
                           'series': character['series']['available'],
                           'events': character['events']['available'],
                           'stories': character['stories']['available'],
                            # 'thumbnail': character['thumbnail'],
                           'name': character['name'],
                           # 'description': character['description'],
                           'citizenship': character.get('wiki', {}).get('citizenship', 'n/a'),
                           'height': character.get('wiki', {}).get('height', 'n/a'),
                           'weight': character.get('wiki', {}).get('weight', 'n/a'),
                           'hair': character.get('wiki', {}).get('hair', 'n/a'),
                           'education': character.get('wiki', {}).get('education', 'n/a'),
                           'occupation': character.get('wiki', {}).get('occupation', 'n/a'),
                           'eyes': character.get('wiki', {}).get('eyes', 'n/a'),
                           'groups': character.get('wiki', {}).get('groups', 'n/a'),
                           'universe': character.get('wiki', {}).get('universe', 'n/a'),
                           'identity': character.get('wiki', {}).get('identity', 'n/a'),
                           })
    return characters

def row_writer(worksheet, row_number, fields):
    for column_number, field in enumerate(fields):
        worksheet.write(row_number, column_number, field)

def export_characters(filename):
    wb = Workbook()
    worksheet = wb.add_sheet('0')
    row_number = 0
    characters = parse_character_files('../characters')
    attributes = ['name', 'comics', 'series', 'events', 'stories',
                  'citizenship', 'weight', 'height', 'hair', 'education',
                  'categories', 'occupation', 'eyes', 'groups', 'universe',
                  'identity'
                 ]

    row_writer(worksheet, row_number, attributes)
    row_number += 1

    for record in characters:
        fields = [record.get(attribute, '') for attribute in attributes]
        row_writer(worksheet, row_number, fields)
        row_number += 1

    wb.save(filename)

export_characters('../characters_all.xls')




