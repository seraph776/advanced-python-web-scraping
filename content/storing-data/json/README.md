<div id="top"  align="center">

# Storing Data
## JSON

</div>

JSON (an acronym for JavaScript Object Notation) is a data-interchange format and is most commonly used for client-server communication. A JSON is an unordered collection of key and value pairs, resembling Python's native dictionary.



```python
import json

# JSON string
str_ = '{"id":"09", "name": "Nitin", "department":"Finance"}'

# Convert string to dict
dict_ = json.loads(str_)

# Convert dict to JSON
json_ = json.dumps(dict_, indent=4)
print(json_)
```
     
# Deserialization (DECODING)
When we convert `JSON` into `Python` objects we call it a JSON  `deserialization` or `parsing`.

## Load vs Loads

- `json.load()` - To parse JSON from `URL` or `file`.
-  `json.loads()` - To parse JSON `string` with content.

# Serialization (ENCODING)

When we encode `Python` Objects into `JSON` we call it a `serialization`.

## Dump vs Dumps

- `json.dump()` - Encodes and write JSON into a file.
- `json.dumps()` - Encodes any Python object into JSON String.

<div align="right">

[[↑] Back to top](#top)

</div>  

