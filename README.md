# Scrapper

Just the first step.
Spider take information from Blizzard's site
(but xpath recvests work with string(looking a little strange)).
Scrapper write down info into database.

How to run:
1. ".//env/scripts/activate"
2. "pip install scrapy"
3. "scrapy runspider blizzard_spider.py <-o info.csv>"