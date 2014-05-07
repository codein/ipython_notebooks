"""
This spider is resposible for fetching tags from for each page

scrapy runspider page_spider.py -o tag_pages_export.json -t json

"""
import json

from scrapy.selector import Selector
from scrapy.spider import Spider
from scrapy.item import Item, Field




class Page(Item):
    page = Field()


class MySpider(Spider):
    name = 'spider'
    allowed_domains = ['infochimps.com']

    tags_file = open('tags.json', 'r+')
    tags_records = json.load(tags_file)
    print tags_records
    tags = set()
    [tags.add(str(tag['text'])) for tag in tags_records]

    page_spider_file = open('page_spider_export.json', 'r+')
    page_records = json.load(page_spider_file)

    page_metadata_map = {}
    start_urls = []
    base_url = 'http://www.infochimps.com'
    for page_record in page_records:
        metadata = {
            'count': page_record['tag']['size'],
            'parent_tag': page_record['tag']['text']
        }

        for page in page_record['tag']['pages']:
            url = '%s%s' % (base_url, str(page['href']))
            metadata['title'] =  page['title']
            page_metadata_map[url] = metadata

            start_urls.append(url)

    def parse(self, response):
        sel = Selector(response)
        tag_elements = sel.xpath('//a[contains(@class, "tag")]/text()')
        bag_of_tags_from_page = []
        for element in tag_elements:
            tag = str(element.extract().split(' ')[0])
            if tag in self.tags:
                bag_of_tags_from_page.append(tag)


        page_object = Page()
        metadata = self.page_metadata_map[response.url]

        page_object['page'] = {
            'url': response.url,
            'tags': bag_of_tags_from_page
        }

        page_object['page'].update(metadata)
        return page_object
