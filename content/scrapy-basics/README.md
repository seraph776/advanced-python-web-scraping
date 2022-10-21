# Scrapy

- `Items` -  Spiders may return the extracted data as items, Python objects that define key-value pairs.
- `Middleware` - A framework of hooks into Scrapy’s spider processing mechanism where you can plug custom functionality to process the responses that are sent to Spiders 
- `Pipelines` - After an item has been scraped by a spider, it is sent to the Item Pipeline which processes it. uses include: 
  - validating scraped data
  - checking for duplicates
  - storing the scraped item in a database
- `Settings` - Allows you to customize the behaviour of all Scrapy components, including the core, extensions, pipelines and spiders themselves


## Start project

```cmd
scrapy startproject `PROJECTNAME`
```

## Create a Spider

Usage: scrapy genspider [options] <name> <domain> 
  
```cmd
scrapy genspider quotes_spider quotes.toscrape.com
```



## Run Spider

```cmd
scrapy crawl SPIDERNAME
```


## Save scraped data

```
scrapy crawl SPRIDERNAME -o filename.csv/json/xml
```





## Pagination

### Method 1

```python

next_page = response.css('li.next a::attr(href)').get()
if next_page is not None:
    yield response.follow(next_page, callback=self.parse)

```

### Method 2

```python
class QuoteSpider(scrapy.Spider):
    name = 'quotes'

    page_number = 2
    start_urls = [
        'https://quotes.toscrape.com/page/1/'
    ]
    
    
    # Further down the code
    
            next_page = f'https://quotes.toscrape.com/page/{QuoteSpider.page_number}/'
        if QuoteSpider.page_number < 11:
            QuoteSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)
```
                                  
## Logging In
                                        
```python
    def parse(self, response, **kwargs):
        token = response.css('form input::attr(value)').extract_first()
        return FormRequest.from_response(response, formdata={
            'csrf_token':token,
            'username': 'seraph',
            'password': 'secret',

        },callback=self.start_scraping)

 
```
                                              
                                        
                                        
