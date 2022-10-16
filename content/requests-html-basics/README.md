<div id="top"  align="center">

# Requests-HTML Module

</div>


##  ☤ Scraping Function 
 
The structure of the `requests-HTML` parsing call goes like this: `variable.attribute.function(*selector*, parameters)`

- The `variable` is the instance that you created using the `.get(url)` function.
- The `attribute` is the type of content that you want to extract (`html` / `lxml`).
- The requests-HTML parser also has many useful built-in methods for SEOs. 


##  ☤ API Documentation 

The following classes are the main interface to **requests_html.**`HTML`
 
- `absolute_links` - All found links on page, in absolute form
- `arender` - Async version of render. _Takes same parameters._
- `base_url` - The base URL for the page
- `encoding` - The encoding string to be used, extracted from the HTML and HTMLResponse headers
- `find` - Given a CSS Selector, returns a list of Element objects or a single one
    - `selector` - CSS Selector to use.
    - `clean` - Whether or not to sanitize the found HTML of <script> and <style> tags.
    - `containing` - If specified, only return elements that contain the provided text.
    - `first` - Whether or not to return just the first result.
    - _encoding` - The encoding format
- `full_text` - The full text content (including links) of the Element or HTML
- `html` - Unicode representation of the HTML content
- `links` - All found links on page, in as–is form.
- `lxml` - lxml representation of the Element or HTML.
- `next` - Attempts to find the next page, if there is one. If fetch is True (default), returns HTML object of next page. If fetch is False, simply returns the next URL
- `raw_html ` - Bytes representation of the HTML content
- `render` - Reloads the response in Chromium, and replaces HTML content with an updated version, with JavaScript executed.
   - `retries` - The number of times to retry loading the page in Chromium.
   - `script` - JavaScript to execute upon page load (optional).
   - `wait` - The number of seconds to wait before loading the page, preventing timeouts (optional).
   - `scrolldown` - Integer, if provided, of how many times to page down.
   - `sleep` - Integer, if provided, of how many seconds to sleep after initial render.
   - `reload` - If `False`, content will not be loaded from the browser, but will be provided from memory.
   - `keep_page` - If `True` will allow you to interact with the browser page through `page.html.page`.
   - `send_cookies_session` - If `True` send `HTMLSession.cookies convert.
   - `cookies` - If not `empty` send `cookies`.

If `scrolldown` is specified, the page will scrolldown the specified number of times, after sleeping the specified amount of time (e.g. `scrolldown=10, sleep=1`).
If just `sleep` is provided, the rendering will wait n seconds, before returning.
If `script` is specified, it will execute the provided JavaScript at runtime.

- `search` -  Search the Element for the given Parse template.
-  search_all` - Search the Element (multiple times) for the given parse template. 
-  `text` - The text content of the Element or HTML 
- `xpath` -  Given an XPath selector, returns a list of Element objects or a single one.
  - `selector` – XPath Selector to use.
  - `clean` – Whether or not to sanitize the found HTML of <script> and <style> tags.
  - `first` – Whether or not to return just the first result.
  - `_encoding` – The encoding format.


<div align="right">

[[↑] Back to top](#top)

</div>  


## ☤  Create a Session

```python
from requests_html import HTMLSession

url = 'https://httpbin.org/'

session = HTMLSession()
page = session.get(url)
```


<div align="right">

[[↑] Back to top](#top)

</div>  



## ☤ Async Session

```python
from requests_html import AsyncHTMLSession
asession = AsyncHTMLSession()

async def get_pythonorg():
    page = await asession.get('https://www.python.org/')

async def get_reddit():
    page = await asession.get('https://reddit.com/')

async def get_google():
    page = await asession.get('https://google.com/')
    
session.run(get_pythonorg, get_reddit, get_google)
```


<div align="right">

[[↑] Back to top](#top)

</div>  


## ☤ Grab a list of links

```python
>>> page.html.links
```


<div align="right">

[[↑] Back to top](#top)

</div>  


## ☤  Grab a list of absolute links

```python
>>> page.html.absolute_links
```


<div align="right">

[[↑] Back to top](#top)

</div>  



## ☤ Select an element with a CSS Selector

```python
>>> element = page.html.find('#element', first=True)
```


<div align="right">

[[↑] Back to top](#top)

</div>  


## ☤ Select an element with a XPath

```python
>>> page.html.xpath('a')
```


<div align="right">

[[↑] Back to top](#top)

</div>  


## ☤ select elements containing certain text

```python
>>> page.html.find('a', containing='keyword')
```



<div align="right">

[[↑] Back to top](#top)

</div>  


## ☤  Grab an element’s text contents

```pythyon
>>> print(page.text)

Eggs
Ham
Spam
```


<div align="right">

[[↑] Back to top](#top)

</div>  


## ☤ Introspect an element’s attributes

```python
>>> page.attrs
{'id': 'page', 'class': ('tier-1', 'element-1'), 'aria-haspopup': 'true'}
```


<div align="right">

[[↑] Back to top](#top)

</div>  


## ☤ Render out an element’s HTML

```python
>>> page.html

<html></html>
```


<div align="right">

[[↑] Back to top](#top)

</div>  


## ☤ Enable JavaScript

```python
>>> page.html.render()
>>> page.html.search('Text to be searched')
```
Or this can be down using async:


```python
>>> await page.html.arender()
>>> page.html.search('Text to be searched')
```


<div align="right">

[[↑] Back to top](#top)

</div>  


## ☤ Pagination

```python
source = session.get('https://reddit.com')
for page in source.html:
    print(page)
```


<div align="right">

[[↑] Back to top](#top)

</div>  
 


## ☤ Utilitiy Function
 
```python  
user_agent = requests_html.user_agent(style='ie')  # chrome, firefox, opera, edge, safari, ie 
```
  
  
 Returns an apparently legit user-agent, if not requested one of a specific style. Defaults to a Chrome-style User-Agent.


<div align="right">

[[↑] Back to top](#top)

</div>  
