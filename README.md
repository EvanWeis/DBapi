# dbAPI.py 

## python SQLite3 API for DDL and DML

Comming form a unix/linux background ive always found Widows powershell to be confusing and cumbersome.
This is especcially true when I work with SQLite3.
Since most of my analysis in is python, I created this API for simple CRUD stuff when I need to do data analysis on my local machine.
It's rudimentary but very easy to use. 


### Usage

the api creates a database in the current working directory by instantiating the `sqlite_datebase` class and executing the `create_connection` method.

### Example

```python

db = sqlite_datebase("some_name.db") #class instance with argument for db name

db.create_connection() #createtion of database file (creates acutal file in current dir)

#sample data formatted as list of tuples
table_data = [
    ("one" "two" 1),
    ("bark" "moo" 500),
    ("apple" "grape" 7),
    ("tree" "grass" 321)
    ]

# name of table to insert
table_name = "test"

#schema or structure of data
schema = """
            first_col TEXT,
            second_col TEXT,
            thrid_col INT,
         """
db.create_table(table_name, schema) # create the table 

db.insert_many(table_name, table_data) # insert the data

db.fetchall(table_name, "*") #retrieve all data in original form of [("one", "two"... ),(...)...]

```