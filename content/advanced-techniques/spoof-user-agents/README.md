<div id="top"  align="center">

# Spoof User-Agents

</div>



A `User-Agent` request header includes a unique string that identifies the browser being used, its version, and the operating system. Their primary function is to decipher which browser are you using to visit a website. They can easily block you, in case you are using a website that isn’t major. You can cut down your chances of getting blacklisted by setting a user agent that seems genuine and well-known. Here is a [database of User-Agents](https://developers.whatismybrowser.com/useragents/explore/) to choose from.


## Google Bot User Agent

```python
USER AGENT  = Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)
```

## Fake-Useragent module

🔥 [fake-useragent](https://pypi.org/project/fake-useragent/) - _included with requests-html_


```python
user_agent = requests_html.user_agent(style='ie')  # chrome, firefox, opera, edge, safari, ie 
```


**Alt Usage**

```python
from fake_useragent import UserAgent

ua = UserAgent()
ua = ua.random
header = {'User-Agent':str(ua)}

htmlContent = requests.get('https://example.com', headers=header)
```



**Get Full Set of Headers** - Sending just a User-Agent wouldn’t be good enough to get past the latest anti-scraping tools and services. The ideal would be to copy it directly from the source. The easiest way to do it is from the Firefox or Chrome DevTools - or equivalent in your browser. Go to the Network tab, visit the target website, right-click on the request and copy as cURL. Then [convert curl syntax to Python](https://curlconverter.com/python/) and paste the headers into the list. To spoof useragents, you can use the following module:

```python
from requests_html import HTMLSession
from fake_useragent import FakeUserAgent

session = HTMLSession()
url = 'https://httpbin.org/headers'

# Get random user-agent
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





<div align="right">

[[↑] Back to top](#top)

</div>  



## Things to Consider 

1. Have the right headers for the browser you are using and the website you are scraping
2. Have a Referer header with the previous page you visited or Google, to make it look real
3. There is no point rotating the headers if you are logging in to a website or keeping session cookies
4. Use proxy servers when making a large number of requests and use a different IP for each browser
5. Spoofing User Agents isn't enough, you must 


<div align="right">

[[↑] Back to top](#top)

</div>  

