import csv

from database import Base, engine, Session
from models import Game


TMP_DATA_STR = '/Users/user19943211/dev/intern_assignment/data/games.csv'


if __name__ == "__main__":
    # check if records already exist and drop if they do
    squery = 'DROP TABLE IF EXISTS games;'
    result = engine.execute(squery)

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
    rows = session.query(Game).count()
    print(f'{rows} records added')
    session.close()

# TODO:
# [ ] add argument for data file path
# [ ] add argument for dialect
