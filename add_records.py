import csv
import sys

from database import engine, session_scope, Base
from models import Game
from sqlalchemy.engine.result import ResultProxy


def drop_table_if_exists(table: str) -> ResultProxy:
    """
        Deletes existing records in database

        Params:
            table: name of table to drop

        Returns:
           sqlalchemy.engine.result.ResultProxy object
    """

    squery = f'DROP TABLE IF EXISTS {table};'
    result = engine.execute(squery)
    return result or None


def add_records_from_file(file_path: str) -> int:
    """
        Creates db entries for each row in a file

        Params:
            file_path: relative or absolute path to file

        Returns
            int: number of rows added to db
    """
    rows_added = 0

    with session_scope() as session:
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

        rows_added = session.query(Game).count()

    return rows_added


def main(data_file: str):
    """
        XXX TODO ADD THIS
    """
    drop_table_if_exists(Game.__tablename__)

    Base.metadata.create_all(engine)


    # open and parse file, add rows to db
    results = add_records_from_file(data_file)
    print(f'{results} records added')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise ValueError('usage: app.py data_file_path')

    main(sys.argv[1])
