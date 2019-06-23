# Database Application (intern assignment)

*Summary*: An application that takes a data source and puts it in a database.  

*Features*:
* can import data from a document
* can parse the contents of a document into db record data
* can add records to a database
* can perform basic queries on the database


## Installation
 [[ TODO ]]


## Running tests  
There are two test suites to run:  
1.  To test the CLI, run `python tests/test_cli.py` from the root project directory  
2.  To run the normal unit tests, run `pytest` from the root project directory

## Sample Usage
1. Add records from a document to a databaseA
*Example*: `$ dbtool import file games.csv psql:chessdb`
*Example*: `$ dbtool import file games.csv psql:chessdb -p games.parser.py`

2. Get summary information about a table
*Usage*: dbtool <action> <target> <summary_type> [-q (SQL query)]
*Example*: `$ dbtool query chessdb total`
*Example*: `$ dbtool query chessdb -q 'victory_status is "mate"`


#:# TO-DO:
* [ ]  add type hints to add_records()


## Questions
*  do I need `setup.py` and to install with `pip install -e`? See pytest docs
*  where should `main` appear in the file structure and do I need a directory with the project name?
*  do I understand imports correctly?
*  how would I persist Resource objects in the real world
