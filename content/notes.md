# Scraping APIs


```python

import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/api/quotes?page'
links = [f'{url}={l}' for l in range(1, 11)]

records = []
#l = ['https://quotes.toscrape.com/api/quotes?page=1', 'https://quotes.toscrape.com/api/quotes?page=2']
for i, link in enumerate(links):

    jsonObj = requests.get(link).json()
    print(f'--------------> Requesting {link}')

    result = jsonObj['quotes']
    for item in result:
        author = item.get('author').get('name')
        quote = item.get('text')
        tags = item.get('tags')
        record = (author, quote, tags)
        records.append(record)


print(len(records))
```
