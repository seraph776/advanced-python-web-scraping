# Writing to a SQLite Database

SQLite is a C library that provides a lightweight disk-based database that doesn’t require a separate server process and allows accessing the database using a nonstandard variant of the SQL query language. 


## Python and SQLite data types

| Datatype  | SQLite Type |
| --------  | --------    |
| `None`    | `Null`      |
| `int`     | `INTEGER`   |
| `float`   | `REAL`      |
| `str`     | `TEXT`      |
| `bytes`   | `BLOB`      |

## Tutorial

```python

import sqlite3

# create a database file
conn = sqlite3.connect("test.db")

# alternatively, create a database in (RAM):
conn = sqlite3.connect(":memory:")

# create a cursor to execuste sql statements
cursor = conn.cursor()

```

## Create SQL statements
Create SQL statements seperately, and as `constants`

```python
CREATE_EMPLOYEE_TABLE = """
    CREATE TABLE employees (
        employeeID INTEGER PRIMARY KEY AUTOINCREMENT,
        firstName TEXT,
        lastName TEXT,
        email TEXT
        );
    """
        
INSERT_EMPLOYEE = "INSERT INTO employees (firstName, lastName, email) VALUES (?, ?, ?);" 
GET_ALL_EMPLOYEES = "SELECT firstName, lastName, email FROM employees;"    
```



## Execute SQL commands
Create `employees` table, and insert `data` into it.

```python
conn.execute(CREATE_EMPLOYEE_TABLE)

data = [("jon", "blackwell", "jblackwell@codecrypt76.com"),
        ("amy", "william", "awilliams@codecrypt76.com"),
        ("lauren", "travis", "ltravis@codecrypt76.com"),
        ]

conn.executemany(INSERT_EMPLOYEE, data)
conn.commit()
```

## Query the database

```python
for row in conn.execute(GET_ALL_EMPLOYEES):
    print(row)
```
### Output

```cmd
('jon', 'blackwell', 'jblackwell@codecrypt76.com')
('amy', 'william', 'awilliams@codecrypt76.com')
('lauren', 'travis', 'ltravis@codecrypt76.com')
```

## Create a function to insert employee data

```python
def insert_employee_data(first_name, last_name, email):
    conn.execute(INSERT_EMPLOYEE, (first_name, last_name, email))


insert_employee_data('elvis', 'presley', 'epresley@codecrypt76.com')
```


## Class Example

```python
class EmployeeDB:

    def __init__(self, name):
        self.connection = sqlite3.connect(name)
        self.cursor = self.connection.cursor()

        create_table_sql = """
            CREATE TABLE employees (
                employeeID INTEGER PRIMARY KEY AUTOINCREMENT,
                firstName TEXT,
                lastName TEXT,
                email TEXT
                );
            """        

        self.cursor.execute(create_table_sql)

    def insert_single_employee(self, first, last, email):
        insert_employee_sql = "INSERT INTO employees (firstName, lastName, email) VALUES (?, ?, ?);"
        self.cursor.execute(insert_employee_sql, (first, last, email))
        self.connection.commit()

    def insert_many_employees(self, employees):
        sql = "INSERT INTO employees (firstName, lastName, email) VALUES (?, ?, ?);"
        self.cursor.executemany(sql, employees)
        self.connection.commit()

    def view_database(self):
        view_all_sql = "SELECT * FROM employees;"
        for row in self.cursor.execute(view_all_sql):
            print(row)

    def get_employee_by_name(self, name):
        select_employee_sql = "SELECT * FROM employees WHERE name =  ?;"
        return self.cursor.execute(select_employee_sql, name)

    def delete_employee_by_id(self, employee_id):
        sql = "DELETE FROM employees WHERE employeeID = ?;"
        self.cursor.execute(sql, employee_id)
        self.connection.commit()


employee_db = EmployeeDB(":memory:")

employee_db.insert_single_employee("jon", "black", "jblackwell@codecrypt76.com")

data = [("mark", "fortune", "mforune@codecrypt76.com"),
        ("amy", "william", "awilliams@codecrypt76.com"),
        ("lauren", "travis", "ltravis@codecrypt76.com"),
        ]

employee_db.insert_many_employees(data)
employee_db.view_database()

```
