import json

from collections import defaultdict
from xlwt import Workbook

page_tags_spider_export = open('../scraping/page_tags_spider_export.json', 'r+')
page_records = json.load(page_tags_spider_export)

print len(page_records)
print page_records[0]
tag_cooccurance_map = {}

for page_record in page_records:
    parent_tag = page_record['page']['parent_tag']
    tags = page_record['page']['tags']
    if parent_tag not in tag_cooccurance_map:
        tag_cooccurance_map[parent_tag] = defaultdict(int)

    cooccurance_map = tag_cooccurance_map[parent_tag]
    for tag in tags:
        cooccurance_map[tag] += 1


# remove self occurance
for tag, cooccurance_map in tag_cooccurance_map.iteritems():
    del cooccurance_map[tag]
    print tag, cooccurance_map

export_file = open('tag_cooccurance_map_esport.json', 'w+')
json.dump(tag_cooccurance_map, export_file, indent=4)

#export for clustering
tag_dimensions = set()
for tag, cooccurance_map in tag_cooccurance_map.iteritems():
    tag_dimensions.add(tag)
    [tag_dimensions.add(tag) for tag, count in cooccurance_map.iteritems()]

tag_dimensions = sorted(tag_dimensions)

def row_writer(worksheet, row_number, fields):
    for column_number, field in enumerate(fields):
        worksheet.write(row_number, column_number, str(field))


workbook = Workbook()
worksheet = workbook.add_sheet('tag_cooccurance_matrix')
headers = ['tag'] + tag_dimensions
nrow = 0
row_writer(worksheet, nrow, headers)

for parent_tag, cooccurance_map in tag_cooccurance_map.iteritems():
    record = [parent_tag]

    for tag in tag_dimensions:
        if tag in cooccurance_map:
            record.append(cooccurance_map[tag])
        else:
            record.append(0)

    nrow += 1
    row_writer(worksheet, nrow, record)

workbook.save('tag_cooccurance_matrix.xls')


# export for flare map
# occurance_flare = []
# added = []
# for parent_tag, cooccurance_map in tag_cooccurance_map.iteritems():
#     imports = []
#     for tag, count in cooccurance_map.iteritems():
#         if tag in tag_cooccurance_map:
#             imports.append(tag)
#         elif tag in added:
#             imports.append(tag)
#         else:
#             added.append(tag)
#             occurance_flare.append({
#                 'name': tag,
#                 'imports': []
#                 })
#             imports.append(tag)

#     print imports
#     occurance_flare.append({
#         'name': parent_tag,
#         'imports': imports
#         })

# export_file = open('tag_cooccurance_flare_export.json', 'w+')
# json.dump(occurance_flare, export_file, indent=4)


