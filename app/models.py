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

    def __init__(self, data):
        for column, datum in data.items():
            try:
                datum = parser_defs[column](datum)
            except KeyError:
                raise KeyError(f'no parser definition exists for "{column}"')

            if column == 'id':
                setattr(self, 'source_id', datum)
            else:
                if hasattr(self, column):
                    setattr(self, column, datum)


def parse_datetime(stamp: str):
    # exponential has to be coerced several times
    stamp = int(float(stamp))
    return datetime.datetime.fromtimestamp(stamp/1000)


parser_defs = {
    'id': lambda x: str(x),
    'rated': lambda x: x.lower() == 'true',
    'created_at': parse_datetime,
    'last_move_at': lambda x: int(float(x)),
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
