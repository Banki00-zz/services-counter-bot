import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from config import *

logger = logging.getLogger('logger')

DATABASE = {
    'drivername': 'postgresql',
    'host': f'{HOST}',
    'port': '5432',
    'username': f'{DB_USERNAME}',
    'password': f'{DB_PASSWORD}',
    'database': f'{DATABASE}'
}

url_engine = create_engine(f"{DATABASE['drivername']}://{DATABASE['username']}:{DATABASE['password']}@{DATABASE['host']}:{DATABASE['port']}/{DATABASE['database']}")

Session = sessionmaker(bind=url_engine)
session = Session()
Base = declarative_base()


def create():
    Base.metadata.create_all(url_engine)
