import csv

from database import Base, engine, Session
from models import Game


TMP_DATA_STR = '/Users/user19943211/dev/intern_assignment/data/games.csv'


if __name__ == "__main__":
    # generate database schema
    Base.metadata.create_all(engine)

    # create new db session
    session = Session()

    with open(TMP_DATA_STR, newline='\n') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            game = Game(row)
            session.add(game)

        session.commit()
        session.close()

# TODO:
# [ ] add argument for data file path
# [ ] add argument for dialect
