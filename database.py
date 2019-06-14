from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
engine = create_engine('postgresql://mepler:Manthony213@localhost:5432/chess')
Session = sessionmaker(bind=engine)


@contextmanager
def session_scope():
    """Provides a context for working with db sessions"""
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
