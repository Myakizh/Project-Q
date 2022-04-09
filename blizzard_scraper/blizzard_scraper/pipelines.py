# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class BlizzardScraperPipeline:
    def __init__(self):
        self.con = sqlite3.connect('base.db')
        self.cur = self.con.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS winners(
            name TEXT,
            title TEXT,
            university TEXT,
            image TEXT
        )''')

    def process_item(self, item, spider):
        self.cur.execute('''INSERT OR IGNORE INTO winners VALUES(?, ?, ?, ?)''', 
            (item['person'], item['title'], item['university'], item['img_url']))
        self.con.commit()
        return item
