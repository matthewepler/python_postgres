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
        for key, value in data:
            if hasattr(self, key):
                setattr(self, key, value)
