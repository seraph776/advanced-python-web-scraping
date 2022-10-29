import scrapy
from ..items import QuotesspiderItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']


    def parse(self, response):
        all_div_quotes = response.css('div.quote')

        items = QuotesspiderItem()

        for div in all_div_quotes:
            quote = div.css('span.text::text').get()
            author = div.css('.author::text').get()
            tags = div.css('.tag::text').getall()

            items['quote'] = quote
            items['author'] = author
            items['tags'] = tags

            yield items

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
