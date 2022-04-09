import scrapy
from blizzard_scraper.items import BlizScraperItem
from scrapy.loader import ItemLoader

class BlizSpider(scrapy.Spider):
    name = 'blizspider'
    allowed_domains = ['worldofwarcraft.com']
    start_urls = ['https://worldofwarcraft.com/en-us/news/23652344/announcing-the-world-of-warcraft-student-art-contest-2020-winners']
    # Second link
    #'https://worldofwarcraft.com/en-us/news/23783665/announcing-the-world-of-warcraft-student-art-contest-2021-winners'

    def parse(self, response):
        
        for i in range(1, 10):

            s1 = "//div[@class='Blog margin-bottom-medium']/div/figure["+ str(i) + "]/figcaption/text()[1]"
            #ss1 = "//div[@class='Blog margin-bottom-medium']/div/figure["+ str(i) + "]/figcaption/p/text()"
            s2 = "//div[@class='Blog margin-bottom-medium']/div/figure["+ str(i) + "]/figcaption/text()[2]"
            s3 = "//div[@class='Blog margin-bottom-medium']/div/figure["+ str(i) + "]/figcaption/em/text()"
            s4 = "//div[@class='Blog margin-bottom-medium']/div/figure["+ str(i) + "]/div/img/@src"
            s5 = "//div[@class='Blog margin-bottom-medium']/div/figure["+ str(i) + "]/video//@src"

            l = ItemLoader(item = BlizScraperItem(), response = response)
            l.add_xpath('title', s1)
            #l.add_xpath('title', ss1)
            l.add_xpath('person', s2)
            l.add_xpath('university', s3)
            l.add_xpath('img_url', s4)
            l.add_xpath('img_url', s5)
            yield l.load_item()