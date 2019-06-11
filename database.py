from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://mepler:Manthony213@localhost:5432/chess')
Session = sessionmaker(bind=engine)
Base = declarative_base()
