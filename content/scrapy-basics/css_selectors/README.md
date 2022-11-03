# Scrapy Shell


## Select by Class 

```
response.css('.text')
```
## Get Text
```
response.css('.text::text').get()
```

## Select by Attribute 
```
response.css('[itemprop="author"]').get()

```

## Get()
- Returns one item
## Getall()
- Returns a list
