# Scrapy

[Scrapy Docs](https://docs.scrapy.org/_/downloads/en/latest/pdf/)

- `Items` -  Spiders may return the extracted data as items, Python objects that define key-value pairs.
- `Middleware` - A framework of hooks into Scrapy’s spider processing mechanism where you can plug custom functionality to process the responses that are sent to Spiders such as setting up `proxies`, `headers`, `user-agents`, etc.).
- `Pipelines` - After an item has been scraped by a spider, it is sent to the Item Pipeline which processes it. Uses include: 
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
scrapy genspider SPIDERNAME WEBSITE.com
```



## Run Spider

```cmd
scrapy crawl SPIDERNAME
```


  
## Selectors
  
Condition using which we can extract data from a website. 
  - `css`
  - `xpath`
  
  
  
## Save scraped data

```
scrapy crawl SPRIDERNAME -o filename.csv/json/xml
```


```cmd
pip install scrapy-user-agents
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
        token = response.css('form input::attr(value)').get()
        return FormRequest.from_response(response, formdata={
            'csrf_token':token,
            'username': 'seraph',
            'password': 'secret',

        },callback=self.start_scraping)

 
```

> 👉 **Note**:   `.get()` and `.getall()` selector methods are now preferred over `.extract_first()` and `.extract().`
                                        
                                        
