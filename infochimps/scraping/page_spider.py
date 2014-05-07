"""
This spider is resposible for fetching pages(upto 5) for each tags

scrapy runspider page_spider.py -o tag_pages_export.json -t json

"""
import json

from scrapy.selector import Selector
from scrapy.spider import Spider
from scrapy.item import Item, Field


class Tag(Item):
    tag = Field()

class MySpider(Spider):
    name = 'spider'
    allowed_domains = ['infochimps.com']
    base_url = 'http://www.infochimps.com/tags'
    start_urls =[]

    tags_file = open('tags.json', 'r+')
    tags = json.load(tags_file)
    url_tag_map = {}
    for tag in tags:
        url = '%s/%s' % (base_url, tag['text'])
        url_tag_map[url] = tag

        start_urls.append(url)


    def parse(self, response):
        sel = Selector(response)
        elements = sel.xpath('//h2/a')
        pages = []
        for element in elements[:5]:
            page = {
                'url': str(element.xpath('./@href')[0].extract()),
                'title': str(element.xpath('./text()')[0].extract())
                }
            print page
            pages.append(page)

        tag_object = Tag()
        tag = self.url_tag_map[response.url]
        tag['pages'] = pages
        tag_object['tag'] = tag
        return tag_object
