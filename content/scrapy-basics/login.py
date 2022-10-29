import scrapy
from ..items import QuotesspiderItem
from scrapy.http import FormRequest

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        token = response.css('form input::attrs(value)').get()
        login_data = {'csrf_token':token,
                      'username': 'seraph',
                      'password': 'secret'}
        return FormRequest.from_response(response, formdata=login_data, callback=self.start_scraping)

    def start_scraping(self, response):
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
