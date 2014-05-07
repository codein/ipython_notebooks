import json

from collections import defaultdict

tags_file = open('tags.json', 'r+')
tag_records = json.load(tags_file)
tag_count_map = {}
for tag_record in tag_records:
    tag_count_map[tag_record['text']] = tag_record['size']


page_tags_spider_export = open('page_tags_spider_export.json', 'r+')
page_records = json.load(page_tags_spider_export)

tags = defaultdict(list)
# [
#   {
#     "name": "a",
#     "count": 9,
#     "key": "a",
#     "pages": [
#       {
#         "name": "qwe",
#         "key": "3314282933124116679",
#         "title": "qwe",
#         "url": "http:\/\/excelramblings.blogspot.com\/2014\/02\/google-universal-analytics-deaktop.html"
#       },
#       {
#         "name": "Abstracting Excel Data",
#         "key": "5781926054518429618",
#         "title": "Abstracting Excel Data",
#         "url": "http:\/\/excelramblings.blogspot.com\/2011\/06\/abstracting-excel-data.html"
#       }

#     ]
#   },

print page_records[0]
for page_record in page_records:
    page = page_record['page']
    for tag in page['tags']:
        tags[tag].append(page)

tag_page_mapping = []
for tag, page_records in tags.iteritems():

    pages = []
    for page_record in page_records:
        if 'parent_tag' in page_record:
            del page_record['parent_tag']

        if 'tags' in page_record:
            del page_record['tags']
        page_record['name'] = page_record['title']
        page_record['key'] = page_record['title']
        # print page_record
        pages.append(page_record)


    mapping = {
        'name': tag,
        'key': tag,
        'count': tag_count_map[tag],
        'pages': pages
    }

    tag_page_mapping.append(mapping)

print tag_page_mapping

tag_file = open('tag.json', 'w+')
json.dump(tag_page_mapping, tag_file, indent=4)