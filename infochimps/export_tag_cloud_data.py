import json

from operator import itemgetter


pages_file = open('tag_pages_export.json', 'r')
pages = json.load(pages_file)

words = []
for page in pages:
    for tag_record in page['tags']:
        tag, size = tag_record.split(' (')
        size = size.replace(')', '')
        size = int(size)
        if size > 50:
            words.append({'text':tag, 'size':size})

words = sorted(words, key=itemgetter('size'), reverse=True)

tag_cloud_file = open('tags_all.json', 'w+')
print len(words)
tag_cloud_file.write(json.dumps(words))