<div id="top"  align="center">


# Common Data Saving Formats for Web Scraping

</div>



**CSV**: The most common format is a Comma Separated Value (CSV) format – most people know how it works and it is easily viewable in various products including and especially Microsoft Excel.

**JSON**: (JavaScript Object Notation) is a lightweight data-interchange format. It is easy for humans to read and write. It is easy for machines to parse and generate according to json.org


**SQL**: Structured Query Language, isn’t really a data format and is very specific to a particular database and database schema or structure.

## What is a good format?

The most universal and flexible format that works in our business as a Data as a Service provider is `JSON` even though `CSV` may be universally more acceptable.



<div align="right">

[[↑] Back to top](#top)

</div>  


## Why not CSV?

CSV works well for data that is structured in 2 dimensions (rows and columns), but a lot of data that we encounter is in multiple dimensions and doesn’t lend itself well to a 2 dimensional spreadsheet format. If the data is 2 dimensional, we encourage the CSV format because most databases can easily import this data. However, when the data is multi-dimensional and if it is semi-structured (i.e. some items have some data and others have some other data).

Let’s say a merchant’s data has products they sell associated with it and one merchant has 1 product and another has 10 products, it is hard to fit this data into a CSV format especially if you don’t know how many products the largest merchant could have.

Do you create a column for each product? How many columns do you create? 10, 100, 100000.. – that is the problem with using the CSV format for such data.

Another example is a data record for a person that has multiple emails or phone numbers, some may have one, some may have 5 or more of each.

CSV is not flexible to cater to variations in the number of columns for each row in the CSV.


<div align="right">

[[↑] Back to top](#top)

</div>  


## Why not SQL?

SQL isn’t really a data format. It is a language (Structured Query Language) to work with databases.

While SQL can be used to import data into Relational Databases, the format is completely dependent upon the Schema (Database and Table structure) used by the Database. The name of the table, the names of the fields and data types of the fields are all specific to a particular instance of the database. Hence there is no universal formats that fits all like JSON.

We can provide SQL based on a particular schema for an additional cost, but it also requires constant maintenance in case the schema changes.

As a result, we discourage the use of SQL as a data format.



<div align="right">

[[↑] Back to top](#top)

</div>  


## How do I work with JSON?

JSON is a very flexible format that doesn’t add to the size of the data as much as XML. It is easy to read and use. It includes both the field names and the values (data) that go into the field.

It can handle multi-dimensional and semi-structured data with ease and you can add or remove any fields with ease.

JSON is also the de-facto format for handling data in APIs. Inputs to APIs are best provided in JSON and the data returned is also handled well in the JSON format.

Most databases and languages have support for or have readily available libraries for importing and exporting JSON. A quick Google search of JSON + <your favorite database name> will ease the fear of people who are used to CSV format.

  
  
<div align="right">

[[↑] Back to top](#top)

</div>  
