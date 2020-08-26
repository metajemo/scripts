from scrapy.crawler import CrawlerProcess
from muziekgebouweindhoven import MuziekGebouwSpider

process = CrawlerProcess(MuziekGebouwSpider)
process.start()


