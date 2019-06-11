from database import Base, Session, engine
from models import Game

# generate database schema
Base.metadata.create_all(engine)

# create new session
session = Session()

# create records
game_one = Game([
    ('source_id', 'abcdef'),
    ('rated', False),
])

# persist data
session.add(game_one)

session.commit()
session.close()
