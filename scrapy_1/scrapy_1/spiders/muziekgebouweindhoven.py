#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scrapy


class MuziekGebouwSpider(scrapy.Spider):
    name = 'muziekgebouweindhoven'

    start_urls = ['https://www.muziekgebouweindhoven.nl/nl/zoekresultaat/?zoekwaarde=pannenkoekconcert']

    def parse(self, response):
        "parsing the list of search results for panenkoekconcert"
        search_entry_tag = 'div.listItemWrapper'
        disabled_button_tag = 'div.dateTimeContainer>div.dateTimeInner>button.btn.btn-unavailable'
        link_tag = 'div.thumb>a::attr("href")'
        # filter out entries that are not sold out or in the past
        for entry in response.css(search_entry_tag):
            if not entry.css(disabled_button_tag).get():
                yield response.follow(entry.css(link_tag)[0],
                                      self.parse_panenkoekconcert)


    def parse_panenkoekconcert(self, response):
        price = response.xpath('/html/body//div/button[@data-content]/text()').extract()[0]
        stripped_unicode_price = self.unicode_and_strip_string(price)
        if self.is_price_below_five_euro(stripped_unicode_price):
            # sent email here
            print 'empty'
        else:
            print 'price for link: {} is too high..: price: {}'.format(response.url, stripped_unicode_price)

    @staticmethod
    def unicode_and_strip_string(string):
       euro_sign = u'\u20ac'.encode('utf-8')
       chars_to_strip = ['\t', '\n', ' ', euro_sign]
       string = u'{}'.format(string).encode('utf-8')
       for char in chars_to_strip:
           string = string.replace(char, '')
       return string

    @staticmethod
    def is_price_below_five_euro(price):
        _price = price.split('-')[-1]
        return int(float(_price)) <=5
