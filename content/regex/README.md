<div id="top"  align="center">

# Regular Expression

</div>




## Functions


| **Functions** | **Description**                                                   |
|---------------|-------------------------------------------------------------------|
| `re.findall`  | Returns a list containing all matches                             |
| `re.finditer` | Return an iterable of match objects (one for each match)          |
| `re.search`   | Returns a Match object if there is a match anywhere in the string |
| `re.split`    | Returns a list where the string has been split at each match      |
| `re.sub`      | Replaces one or many matches with a string                        |
| `re.compile`  | Compile a regular expression pattern for later use                |
| `re.escape`   | Return string with all non-alphanumerics backslashed              |



<div align="right">

[[↑] Back to top](#top)

</div>  



## Flags

| **Flags**       | **Description**                            |
|-----------------|--------------------------------------------|
| `re.IGNORECASE` | Ignore case                                |
| `re.MULTILINE`  | Multiline                                  |
| `re.LOCALE`     | Make `\w`,`\b`,`\s` locale dependent       |
| `re.DOTALL`     | Dot matches all (including newline         |
| `re.UNICODE`    | Make `\w`,`\b`,`\d`,`\s` unicode dependent |
| `re.VERBOSE`    | Readable style                             |




<div align="right">

[[↑] Back to top](#top)

</div>  


## Anchors

| **Anchors** | **Description**                                         |
|-------------|---------------------------------------------------------|
| `^`         | Start of string, or start of line in multi-line pattern |
| `\A`        | Start of string                                         |
| `$`         | End of string, or end of line in multi-line pattern     |
| `\Z`        | End of string                                           |
| `\b`        | Word boundary                                           |
| `\B`        | Not word boundary                                       |
| `\<`        | Start of word                                           |
| `\>`        | End of word                                             |




<div align="right">

[[↑] Back to top](#top)

</div>  


## Quantifiers

| **Quantifiers** | **Description** |
|-----------------|-----------------|
| `*`             | 0 or more       |
| `+`             | 1 or more       |
| `?`             | 0 or 1          |
| `{3}`           | Exactly 3       |
| `{3,}`          | 3 or more       |
| `{3,5}`         | 3, 4 or 5       |





<div align="right">

[[↑] Back to top](#top)

</div>  


## Character Classes

| **Character Classes** | **Description**   |
|-----------------------|-------------------|
| `\s`                  | whitespace        |
| `\S`                  | Not whitespace    |
| `\d`                  | Digit             |
| `\D`                  | Not digit         |
| `\w`                  | Word              |
| `\W`                  | Not word          |
| `\x`                  | Hexadecimal digit |
| `\O`                  | Octal digit       |





<div align="right">

[[↑] Back to top](#top)

</div>  


# Example


```python
import re
from requests_html import HTMLSession

URL = 'https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'

session = HTMLSession()
page = session.get(URL)


pattern = re.compile(r'\d+')


in_stock_ = page.html.find('.instock', first=True).text
# In stock (22 available)

value = re.search(pattern, in_stock_).group()
print(value)  # 22

```



<div align="right">

[[↑] Back to top](#top)

</div>  

