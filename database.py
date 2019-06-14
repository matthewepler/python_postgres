from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


class DataAccessLayer:
    Base = declarative_base()
    conn_string = None
    engine = None
    Session = None

    def db_init(self, conn_string):
        self.engine = create_engine(conn_string or self.conn_string)
        self.Session = sessionmaker(bind=self.engine)
        self.Base.metadata.create_all(self.engine)


dal = DataAccessLayer()


@contextmanager
def session_scope():
    """Provides a context for working with db sessions"""
    session = dal.Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
