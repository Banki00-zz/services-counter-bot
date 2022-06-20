import logging

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session


logger = logging.getLogger('logger')

DATABASE_NAME = 'services.sqlite'

engine = create_engine(f'sqlite:///{DATABASE_NAME}')
session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()


def create_db():
    Base.metadata.create_all(engine)



