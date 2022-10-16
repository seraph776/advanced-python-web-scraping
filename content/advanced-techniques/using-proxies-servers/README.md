<div id="top"  align="center">

# Using Proxy Servers

</div>





Multiple requests coming from the same IP will lead you to get blocked, which is why we need to use multiple addresses. When we send requests from a proxy machine, the target website will not know where the original IP is from, making the detection harder. By using a proxy, you can change your IP address and user agent to look like a different person on the website. It will help you avoid being detected as a bot and getting caught in a honeypot trap.


## Basic Usages


```python
from requests_html import HTMLSession

session = HTMLSession()
proxy = '71.86.129.131:8080'

r = session.get('http://toscrape.com', proxies={'http':proxy, 'https':proxy}, timeout=3)

print(r.ok)  # True
```
The proxies dictionary must follow this scheme. It is not enough to define only the proxy address and port. You also need to specify the protocol. You can use the same proxy for multiple protocols.



<div align="right">

[[↑] Back to top](#top)

</div>  

## Rotating Proxies

To be able to rotate IPs, we first need to have a pool of IP addresses. You can use free proxies that we can find on the internet or we can use commercial solutions for this. Here is a list of a few free proxy-sites
- [Free-Proxy-List.net](https://free-proxy-list.net/)
- [Free Proxy Lists.net](https://www.freeproxylists.net/)
- [Http Proxies](https://www.proxy-list.download/HTTP)
- [Hide My Name](https://hidemy.name/en/proxy-list/)
- [Proxy-nova](https://www.proxynova.com/proxy-server-list)





> 👉 **Note**: Be aware, that if your product/service relies on scraped data a free proxy solution will probably not be enough for your needs. If a high success rate and data quality are important for you, you should choose a paid proxy solution.


Once you have you list of proxies, you can randomly pick a proxy to use for a session.

```python
import random
import requests.exceptions
from requests_html import HTMLSession

session = HTMLSession()
proxies = ['197.14.14.238:80', '103.17.182.14:9191', '96.95.164.41:3128', '198.74.56.87:8080', '71.86.129.131:8080']

try:
    proxy = random.choice(proxies)
    r = session.get('http://toscrape.com', proxies={'http':proxy, 'https':proxy}, timeout=3)
    print(r.ok)  # True
except requests.exceptions.RequestException as e:
    raise SystemExit(e)
```

> 👉 **Note**: If you are using `rotating proxies`, each request might have a different IP from different regions or countries. Antibots can see that pattern and block it since it's not a natural way for users to browse. 

However, once bypassed the antibot solution, it will send valuable cookies. Defensive systems won't check twice if the session looks legit.

<div align="right">

[[↑] Back to top](#top)

</div>  


### Scrape Free Proxy List

This script will scrape proxies generate from [Free-Poxy-List.net](https://free-proxy-list.net/) and save it to `proxy-list.csv`.


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



<div align="right">

[[↑] Back to top](#top)

</div>  

