# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['muziekgebouweindhoven.nl']
    start_urls = ['https://www.muziekgebouweindhoven.nl/nl/zoekresultaat/?zoekwaarde=pannenkoekconcert']

    def parse(self, response):
        print 'The response: {0}'.format(response.text)
