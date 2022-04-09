# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose

def strip(value) :
    return value.strip()

class BlizScraperItem(scrapy.Item):
    # define the fields for your item here like:
    person = scrapy.Field(input_processor = MapCompose(strip), output_processor = TakeFirst())
    university = scrapy.Field(input_processor = MapCompose(), output_processor = TakeFirst())
    title = scrapy.Field(input_processor = MapCompose(strip), output_processor = TakeFirst())
    img_url = scrapy.Field(input_processor = MapCompose(), output_processor = TakeFirst())