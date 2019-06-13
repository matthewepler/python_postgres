import datetime

from sqlalchemy import Column, String, Integer, Boolean, DateTime

from database import Base


class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True)
    source_id = Column(String)
    rated = Column(Boolean)
    created_at = Column(DateTime)
    last_move_at = Column(DateTime)
    turns = Column(Integer)
    victory_status = Column(String)
    winner = Column(String)
    increment_code = Column(String)
    white_id = Column(String)
    white_rating = Column(Integer)
    black_id = Column(String)
    back_rating = Column(Integer)
    moves = Column(String)
    opening_eco = Column(String)
    opening_name = Column(String)
    opening_ply = Column(Integer)

    def __init__(self, data):
        for column, datum in data.items():
            try:
                datum = parser_defs[column](datum)
                if column == 'id':
                    setattr(self, 'source_id', datum)
                else:
                    if hasattr(self, column):
                        setattr(self, column, datum)
            except KeyError:
                raise KeyError(f'the column header "{column}" is not valid')


def parse_datetime(stamp: str):
    stamp = int(float(stamp))
    try:
        result = datetime.datetime.fromtimestamp(stamp/1000)
    except ValueError:
        print(f'could not coerce {stamp} to datetime object')
        raise
    return result


parser_defs = {
    'id': lambda x: str(x),
    'rated': lambda x: x.lower() == 'true',
    'created_at': parse_datetime,
    'last_move_at': parse_datetime,
    'turns': lambda x: int(x),
    'victory_status': lambda x: str(x),
    'winner': lambda x: str(x),
    'increment_code': lambda x: str(x),
    'white_id': lambda x: str(x),
    'white_rating': lambda x: int(x),
    'black_id': lambda x: str(x),
    'black_rating': lambda x: int(x),
    'moves': lambda x: str(x),
    'opening_eco': lambda x: str(x),
    'opening_name': lambda x: str(x),
    'opening_ply': lambda x: int(x)
}
