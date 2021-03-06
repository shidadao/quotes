# -*- coding: utf-8 -*-
import scrapy

from quotes.items import QuotesItem


class QuotesSpiderSpider(scrapy.Spider):
    name = 'quotes_spider'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.css('.quote')
        for quote in quotes:
            text  = quote.css('.text::text').extract_first()
            author = quote.css('.author::text').extract_first()
            tags =quote.css('.tags .tag::text').extract()



            item = QuotesItem()
            item['text'] = text
            item['author'] = author
            item['tags'] = tags
            yield item

        next = response.css('.pager .next a::attr(href)').extract_first()
        next_url = response.urljoin(next)
        yield scrapy.Request(url = next_url,callback = self.parse)


