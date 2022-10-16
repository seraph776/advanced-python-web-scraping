<div id="top"  align="center">

# Storing Data
## CSV

</div>


## CSV Reader

Reading from a CSV file is done using the `reader` object. The CSV file is opened as a text file with Python’s built-in `open()` function, which returns a file object. This is then passed to the `reader`.


```python

import csv

with open('data_file.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]}, {row[1]} , {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')
```


### Reading CSV Files Into a Dictionary With csv

Rather than deal with a list of individual `String` elements, you can read CSV data directly into a dictionary 

```python
import csv

with open('data_file.txt', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(f'\t{row["column1"]}, {row["Column2"]}, {row["Column3"]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')
```

### Optional Python CSV reader Parameters

- `delimiter` specifies the character used to separate each field. The default is the comma (`','`).
- `quotechar` specifies the character used to surround fields that contain the delimiter character. The default is a double quote (`' " '`).
- `escapechar` specifies the character used to escape the delimiter character, in case quotes aren’t used. The default is no escape character.


## CSV Writer

You can also write to a CSV file using a writer object and the `.write_row()` method:

```python

import csv


with open('output.csv', mode='w', newline='', encoding='utf8') as file:
    csvWriter = csv.writer(file, delimiter='\n', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csvWriter.writerow(['Column1', 'Column2'])

    row = ('firstName', 'lastName')

    csvWriter.writerow(row)
```

The `quotechar` optional parameter tells the `writer` which character to use to quote fields when writing. Whether quoting is used or not, however, is determined by the `quoting` optional parameter:

- If `quoting` is set to `csv.QUOTE_MINIMAL`, then `.writerow()` will quote fields only if they contain the delimiter or the `quotechar`. This is the default case.

If quoting is set to `csv.QUOTE_ALL`, then `.writerow()` will quote all fields.
If quoting is set to `csv.QUOTE_NONNUMERIC`, then `.writerow()` will quote all fields containing text data and convert all numeric fields to the float data type.
If quoting is set to `csv.QUOTE_NONE`, then `.writerow()` will escape delimiters instead of quoting them. In this case, you also must provide a value for the escapechar optional parameter.



## CSV DictReader

```python
import csv

with open('output.csv', mode='r') as csv_file: 
    dictReader = csv.DictReader(csv_file)

    next(dictReader)

    for item in dictReader:
        print(item['Column1'])
```



## CSV DictWriter

It is possible to write data from a dictionary as well:


```python
import csv

with open('output.csv', mode='w') as csv_file:
    fieldnames = ['Column1', 'Column2', 'Column3']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    
    row = {'Column1': 'John', 'Colmun2': 'Blackwell', 'Column3': 'admin@codecrypt76.com'}
    
    writer.writerow(row)

```
