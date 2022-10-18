<div align="center">

# Resources

</div>




## Web Scraping Test Sites

- [Books to Scrape](http://books.toscrape.com/)
- [Quotes to Scrape](http://quotes.toscrape.com/)
- [Scrape This Site](https://www.scrapethissite.com/)
- [Fake Python Jobs](https://realpython.github.io/fake-jobs/)
- [Web Scraper Test Sites](https://webscraper.io/test-sites)

## Web Scraping Challenges

- [Scrape World](https://scrape.world/)
- [W3Resource Exefcises](https://www.w3resource.com/python-exercises/BeautifulSoup/index.php)


## Freelance Work

- [Upwork](https://www.upwork.com)
- [Freelancer](https://www.freelancer.com/)
- [Fiverr](https://www.fiverr.com/)
- [PeoplePerHour](https://www.peopleperhour.com/)
- [SolidGigs](https://solidgigs.com/)
- [Guru](https://www.guru.com/)


## Old TOC


<details>

<summary>Click </summary>

- Useful Libraries
- Making Simple Requests
- Inspecting the Response
- Extracting Content from HTML
  - Using Regular Expressions
  - Using BeautifulSoup
  - Using XPath Selectors
- Storing Your Data
- Writing to a CSV
- Writing to a SQLite Database
- More Advanced Topics
  - Javascript Heavy Websites
  - Content Inside iFrames
  - Sessions and Cookies
  - Delays and Backing Off
  - Spoofing the User Agent
  - Using Proxy Servers
  - Setting Timeouts
  - Handling Network Errors

</details>  

## Old Content


## Element Methods

- #### Get Element `TEXT`
```python
print(element.text)
```
- #### Get Element `ATTRIBUTES`

```python
print(element.attrs)
print(element.attrs['href'])
```

- #### Get Element `ABSOLUTE URL`
```python
print(element.absolute_links.pop())
```

- #### Get Element `TAG`
```python
print(element.tag)
```

- #### Reneder Element's `HTML` 
```python
print(element.html)
```


## Find Elements

- #### Using `find()` - Given a CSS Selector, returns a list of Element objects or a single one
  - `selector`  - CSS Selector to use.
  - `clean` – Whether or not to sanitize the found HTML of <script> and <style> tags.
  - `containing` – If specified, only return elements that contain the provided text.
  - `first` – Whether or not to return just the first result.
  - `_encoding` – The encoding format.
- #### Using `xpath()` - Given an XPath selector, returns a list of Element objects or a single one
  - _same parameters as find_
- #### Using `search()` - Search for text on the page
```python
element.('Python is a {} language')[0]  
# programming
```


  
  
  (method, url, params=None, data=None, headers=None, cookies=None, files=None, auth=None, timeout=None, allow_redirects=True, proxies=None, hooks=None, stream=None, verify=None, cert=None, json=None)
