from contextlib import redirect_stdout
import csv
import os
import sys

from database import Base, engine, Session
from models import Game


def drop_table_if_exists(table: str):
    squery = f'DROP TABLE IF EXISTS {table};'
    result = engine.execute(squery)
    return result


def add_records_from_file(file_path: str):
    # create new db session
    session = Session()

    # DictReader parses each row into an OrderedDict
    # as keys and cell data as values
    try:
        with open(file_path, newline='\n') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                game = Game(row)
                session.add(game)
    except FileNotFoundError as fnf_error:
        print(fnf_error)
        raise

    # write changes to db
    session.commit()

    rows_added = session.query(Game).count()
    session.close()

    return rows_added


if __name__ == "__main__":
    # check for passed arguments
    if len(sys.argv) != 2:
        print('usage: app.py data_file_path')
        exit()

    data_file = sys.argv[1]

    drop_table_if_exists(Game.__tablename__)

    # generate database schema(s)
    Base.metadata.create_all(engine)

    results = add_records_from_file(data_file)
    print(f'{results} records added')


# TODO:
# [ ] break out parser docs into a separate file
# [ ] make into executable package
# [ ] add docstrings and comments where necessary
