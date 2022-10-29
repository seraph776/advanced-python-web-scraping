import scrapy
from ..items import QuotesspiderItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    page_number = 2
    start_urls = ['https://quotes.toscrape.com/page/1/']

    # -------------------------------
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

        next_page = f'https://quotes.toscrape.com/page/{QuotesSpider.page_number}'
        if QuotesSpider.page_number <= 11:
            QuotesSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)
