
# CSVFeedSpider

It iterates through each of its rows, receives a CSV file as a response, and calls `parse_row()` method. It has the following class:


```python
from scrapy.spiders import CSVFeedSpider
from demoproject.items import DemoItem

class DemoSpider(CSVFeedSpider):
    name = "demo"
    allowed_domains = ["www.demoexample.com"]
    start_urls = ["http://www.demoexample.com/feed.csv"]
    delimiter = ";"
    quotechar = "'"
    headers = ["product_title", "product_link", "product_description"]
    
    def parse_row(self, response, row):
        self.logger.info("This is row: %r", row)
        item = DemoItem()
        item["product_title"] = row["product_title"]
        item["product_link"] = row["product_link"]
        item["product_description"] = row["product_description"]
        return item

```

```python
class scrapy.spiders.CSVFeedSpider
```
