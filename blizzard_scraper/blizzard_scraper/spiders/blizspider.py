import scrapy


class BlizspiderSpider(scrapy.Spider):
    name = 'blizspider'
    allowed_domains = ['blizdomain.com']
    start_urls = ['http://blizdomain.com/']

    def parse(self, response):
        pass
