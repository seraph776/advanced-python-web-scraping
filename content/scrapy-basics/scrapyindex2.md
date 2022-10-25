
## Select element by class

```python
response.css("div.price").get()
```


## Select element by id

```python
response.css("p#color").get()
```


## Select element by attribute

```python
response.css("a[href]").get()
response.css("h3 a").attrib['title']).get()
```

## Select element by attribute using XPath

```python
response.xpath("//a[@title]").get()

response.xpath("//p[@class='color']").get()
```

## Xpath Text()

```python
response.xpath("//h3/a/text()").get()
```

```python
response.xpath("//h3/a/@title").get()
```
