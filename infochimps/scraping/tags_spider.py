"""
This Spider is responsible for fetching the tags and their frequecies from infochimps.com
scrapy runspider tags_spider.py -o export.json -t json
"""

from scrapy.selector import Selector
from scrapy.spider import Spider

from scrapy.item import Item, Field

class Page(Item):
    tags = Field()

class MySpider(Spider):
    name = 'spider'
    allowed_domains = ['infochimps.com']
    base_url = 'http://www.infochimps.com/tags'
    start_urls =[]
    for page_no in xrange(1, 213):
        url = '%s?page=%s' % (base_url, page_no)
        start_urls.append(url)

    def parse(self, response):
        sel = Selector(response)
        elements = sel.xpath('//a[contains(@class, "tag")]/text()')
        page = Page()
        page['tags'] = [element.extract() for element in elements]
        return page
