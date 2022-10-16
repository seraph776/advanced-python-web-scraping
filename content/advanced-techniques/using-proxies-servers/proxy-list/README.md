<div id="top"  align="center">


# Scrape Free Proxy List

</div>


This script will scrape proxies generate from [Free-Poxy-List.net](https://free-proxy-list.net/) and save it to [proxy-list.csv](https://github.com/seraph776/advanced-python-web-scraping/blob/main/content/advanced-techniques/using-proxies-servers/proxy-list/free-proxy-list.csv).


```python
#!/usr/bin/env python3
import csv
from requests_html import HTMLSession

session = HTMLSession()
page = session.get('https://free-proxy-list.net/').html

headers = [tag.text for tag in page.find('thead', first=True).find('th')][:-1]
table_rows = page.find('tbody', first=True).find('tr')

ht = {'yes': True, 'no': False}

proxy_list = []
for col in table_rows:
    ip_address = col.find('td')[0].text
    port = col.find('td')[1].text
    code = col.find('td')[2].text
    country = col.find('td')[3].text
    anonymity = col.find('td')[4].text
    google = ht.get(col.find('td')[5].text)
    https = ht.get(col.find('td')[6].text)
    row = {'IP Address': ip_address,
           'Port': port,
           'Code': code,
           'Country': country,
           'Anonymity': anonymity,
           'Google': google,
           'Https': https
           }
    proxy_list.append(row)

with open(file='proxy-list.csv', mode='w', encoding='utf8', newline='') as file:
    dictWriter = csv.DictWriter(file, fieldnames=headers)
    dictWriter.writeheader()

    for row in proxy_list:
        dictWriter.writerow(row)
```
