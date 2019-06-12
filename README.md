TO-DO
-----
* [ ] connect to database with sqlalchemy
* [ ] create .env file or equivalent
* [ ] test CRUD on new database

* [ ] Create a Move class and a corresponding many to many relationship with
  Game

# Approach
    The program should:
        1.) import data from a file
        2.) take a file argument
        3.) give feedback on the success of the data import
        4.) allow the user to make simple queries

# Assignment #1 - Instructions

*    ✓ Find a relatively simple dataset that you can work with and perform some sort of aggregation on, such as movie scores, movie reviews, sporting event stats, web server stats, etc.
*    ✓ Pick a dataset with a lot of different distinct entities (different movies, candies, etc.).
*    ✓ Pick a dataset with a standard numerical range as a rating or average of some field within the data.
*    ✓ Pick a dataset not too small, not too large. (5k rows < num < 1m rows)
*    ✓ Try to save the dataset to disk so you’re not requesting the data from an API or web site each time you run your script.
*    Write a script to ingest that data from a file and save to a database. (SQLite, PostgreSQL, MySQL/MariaDB)
*    ✓ Don’t worry about adding indexes at this point.
*    Write a script to output basic stats about that data from the database to prove the visibility and accessibility of the data.
*    Push your code to your personal GitLab repo. (call it “onboarding” or something)
*    Set up linting and testing and get your build to be successful/green. (see https://gitlab.s.fpint.net/collections/bmt/blob/master/.gitlab-ci.yml and https://gitlab.s.fpint.net/collections/bmt/blob/master/prova.unit.yml )

# Dev Notes
## Why SQLAlchemy?
1.  SQLAlchemy does not duplicate what a DBAPI controller like psycopg2 does, but make it easier to write.
2.  It provides more portability. I could switch to a totally different database engine without having to make significant changes.
3.  Added benefit of an ORM without losing the ability to write complex or
    custom queries in raw SQL
4.  Seems to be more prevalant in the real-world than just using a database
    controller
5.  The abstractions do not detract from my understanding of how the database
    is working, but they do help me write code that is more pythonic and
    readable. This is passed on to the next developer.
