from sqlalchemy import Column, String, Integer, Boolean, DateTime

from database import Base
from parser import parser_defs


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
            except KeyError:
                raise KeyError(f'the column header "{column}" is not valid')
            else:
                if column == 'id':
                    setattr(self, 'source_id', datum)
                else:
                    if hasattr(self, column):
                        setattr(self, column, datum)

