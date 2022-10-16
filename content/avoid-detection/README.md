<div id="top"  align="center">

# How to Avoid Detection

</div>


## Avoid Logging in

Login is basically permission to get access to web pages. If a page is protected by login, the scraper would have to send some information or cookies along with each request to view the page. This makes it easy for the target website to see requests coming from the same address. They could take away your credentials or block your account which can, in turn, lead to your web scraping efforts being blocked.

- IP Rate Limit
- Rotating Proxies



<div align="right">

[[↑] Back to top](#top)

</div>  



## Use Headless browser

A headless browser is a web browser without a graphical user interface. Headless browsers are often used for automated testing and web scraping. They are fast and can be controlled programmatically. Using a headless browser will help you avoid honeypot traps because they make it harder for websites to detect that you’re a bot. There are libraries to automatically control browsers such as the following:



| Name                                                                | About                                                                                       |
| ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| [Jabba-Webkit](https://github.com/jabbalaci/Jabba-Webkit)           | Jabba's headless webkit browser for scraping AJAX-powered webpages.                         |
| [MechanicalSoup](https://github.com/MechanicalSoup/MechanicalSoup)  | A Python library for automating interaction with websites.                                  |
| [mechanize](https://wwwsearch.sourceforge.net/mechanize/)           | Stateful programmatic web browsing.                                                         |
| [phantompy](https://github.com/niwinz/phantompy)                    | Phantompy is a headless WebKit engine with powerful pythonic api build on top of Qt5 Webkit |
| [RoboBrowser](https://github.com/jmcarp/robobrowser)                | A simple, Pythonic library for browsing the web without a standalone web browser.           |
| [Spynner](https://github.com/makinacorpus/spynner)                  | Programmatic web browsing module with AJAX support for Python                               |




<div align="right">

[[↑] Back to top](#top)

</div>  


## Spoof User-Agents

A User-Agent request header includes a unique string that identifies the browser being used, its version, and the operating system. Their primary function is to decipher which browser are you using to visit a website. They can easily block you, in case you are using a website that isn’t major. You can cut down your chances of getting blacklisted by setting a user agent that seems genuine and well-known. Here is a [database of User-Agents](https://developers.whatismybrowser.com/useragents/explore/) to choose from.

**Get Full Set of Headers** - Sending just a User-Agent wouldn’t be good enough to get past the latest anti-scraping tools and services. The ideal would be to copy it directly from the source. The easiest way to do it is from the Firefox or Chrome DevTools - or equivalent in your browser. Go to the Network tab, visit the target website, right-click on the request and copy as cURL. Then [convert curl syntax to Python](https://curlconverter.com/python/) and paste the headers into the list. To spoof useragents, you can use the following module:

```python
from requests_html import HTMLSession
from fake_useragent import FakeUserAgent

session = HTMLSession()

url = 'https://httpbin.org/headers'
user_agent = FakeUserAgent().random

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "Dnt": "1",
    "Host": "httpbin.org",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": user_agent,
}

r = session.get(url, headers=headers)
print(headers)
print(r.json())

# Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/5.0 Opera 11.11
# {'headers': {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8', 'Dnt': '1', 'Host': 'httpbin.org', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/5.0 Opera 11.11', 'X-Amzn-Trace-Id': 'Root=1-6345dbc9-4487f95b4e185c021c773970'}}

```


🔥 [Fake-Useragent](https://pypi.org/project/fake-useragent/)


```python
from fake_useragent import UserAgent

ua = UserAgent()
ua = ua.random
header = {'User-Agent':str(ua)}

htmlContent = requests.get('https://example.com', headers=header)
```

**Things to keep in mind while Spoofing User Agents**

1. Have the right headers for the browser you are using and the website you are scraping
2. Have a Referer header with the previous page you visited or Google, to make it look real
3. There is no point rotating the headers if you are logging in to a website or keeping session cookies
4. Use proxy servers when making a large number of requests and use a different IP for each browser
5. Spoofing User Agents isn't enough, you must 


<div align="right">

[[↑] Back to top](#top)

</div>  


## Store cookies

## Using Proxy Servers

Multiple requests coming from the same IP will lead you to get blocked, which is why we need to use multiple addresses. When we send requests from a proxy machine, the target website will not know where the original IP is from, making the detection harder. By using a proxy, you can change your IP address and user agent to look like a different person on the website. It will help you avoid being detected as a bot and getting caught in a honeypot trap.


**Basic Usages:**


```python
from requests_html import HTMLSession

session = HTMLSession()
proxy = '71.86.129.131:8080'

r = session.get('http://toscrape.com', proxies={'http':proxy, 'https':proxy}, timeout=3)

print(r.ok)  # True
```
The proxies dictionary must follow this scheme. It is not enough to define only the proxy address and port. You also need to specify the protocol. You can use the same proxy for multiple protocols.

**Rotating Proxies:**

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


## Set A Referrer

The referrer header is an http request header that informs the website where you are previously visiting from. This can be your lifesaver during any web scraping operation. Your goal should be to appear as if you are coming directly from google. By setting this as `https://www.google.co.uk`, it therefore looks like you’re arriving from the UK Google search engine.

- `“Referer”: “https://www.google.co.uk“`

You can also change this to be specific for different countries, i.e:

- US: `“Referer”: “https://www.google.com“`
- Spain: `“Referrer”: “https://www.google.es“`


- Geographic Limits or Geoblocking
- Behavioral patterns
- Using Google cache



<div align="right">

[[↑] Back to top](#top)

</div>  


## Use a CAPTCHA Solving Service

Captchas are one of the most widely used anti-scraping tools. Most of the time, crawlers cannot bypass the captchas on websites. 
By using a CAPTCHA service, you can significantly reduce the chance that a website thinks you’re a web bot.  Simple text-based captchas can be solved by using Optical Character Recognition (OCR); you can use [pytesseract](https://github.com/madmaze/pytesseract) python library for solving captchas. Solving captchas is considerable overhead in the scraping process, so if you want to get rid of this overhead you can employ the help of APIs such as:

- [AntiCAPTCHA](https://anti-captcha.com/)
- [DeathByCaptcha](https://www.deathbycaptcha.com/)
- [2Captcha](https://2captcha.com/)

Good artcile on [How to bypass CAPTCHAS](https://cloudsek.com/how-to-bypass-captchas-easily-using-python-and-other-methods/)


<div align="right">

[[↑] Back to top](#top)

</div>  


## Scrape Slowly

When using web scraping services, it’s tempting to the scrape data as fast as possible. However, when a human stays on a website, their browsing speed is quite slow compared to crawlers. Also, website owners can often detect your scrapers by analysing:

- How fast you scroll on pages.
- How often you click and navigate on the pages.
- If you’re interacting with the pages too fast, the site most likely is going to block you.


<div align="right">

[[↑] Back to top](#top)

</div>  


## Add Random Sleep Delays

A web scraper is like a robot. Web scraping tools will send requests at regular intervals of time. Your goal should be to appear as human as possible. Since humans don’t like routine, it is better to space out your requests at random intervals. This way, you can easily dodge any anti-scraping tool on the target website. It’s best practice to fine tune your website crawlers and to:

- Add in random sleep delays between your HTTPS requests.
- Add in random breaks / delays whilst interacting with JavaScript content to emulate the behaviour of a standard user.


<div align="right">

[[↑] Back to top](#top)

</div>  

## Advanced Search Operators in Google

Use advanced search operators in Google to manually find the URL patterns mentioned above.

Using the `site:` operator, you tell search engines to search within a certain domain only, while `inurl`: indicates you're only looking for pages with a certain URL pattern.

Example queries:

- `site:example.com inurl:filter`
- `site:example.com inurl:wishlist`
- `site:example.com inurl:favorite`
- `site:example.com inurl:cart`
- `site:example.com inurl:search`
- `site:example.com inurl:sessionid`

you can also combine this into one query. In this example we've combined all six of the URL patterns above for amazon.com.

```
https://www.google.com/search?ei=FthRW7SvPITbwQKB2rfIDw&q=site%3Aamazon.com+inurl%3Afilter+OR+inurl%3Awishlist+OR+inurl%3Afavourite+OR+inurl%3Acart+OR+inurl%3Asearch+OR+inurl%3Asessionid&oq=site%3Aamazon.com+inurl%3Afilter+OR+inurl%3Awishlist+OR+inurl%3Afavourite+OR+inurl%3Acart+OR+inurl%3Asearch+OR+inurl%3Asessionid&gs_l=psy-ab.3...9745.27087.0.27574.84.69.8.0.0.0.362.3395.52j8j0j1.61.0....0...1c.1.64.psy-ab..15.0.0....0.9tQcmAcq-8s
```


<div align="right">

[[↑] Back to top](#top)

</div>  

##  Follow Best Practices

Being a good digital citizen will help you avoid many honeypots. Whenever you’re scraping a website, do the following:
- Check the TOS regarding their web scraping preferences.
- Scrape during off - hours to avoid overloading the server.
- Don’t be greedy — only collect the data you need.
- Use an ethical proxy provider.
- Program your scraper to space out requests.
- Follow the robots.txt instructions.



<div align="right">

[[↑] Back to top](#top)

</div>  
