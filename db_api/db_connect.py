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

url_engine = create_engine("postgresql://pbxqwhyzhqfnbd:a6f8c96e415919d2b44cb8c67c5547710efabfb75bfa742226f695e46b4707b6@ec2-34-252-216-149.eu-west-1.compute.amazonaws.com:5432/d4fsoh9lmtgd1n")


# def get_engine(dict:DATABASE):
#     url = f"{dict['drivername']}://{dict['username']}:{dict['password']}@{dict['host']}:{dict['port']}/{dict['database']}"
#     if not database_exists(url):
#         create_database(url)
#     engine = create_engine(url)
#     return engine


Session = sessionmaker(bind=url_engine)
session = Session()
Base = declarative_base()


def create():
    Base.metadata.create_all(url_engine)
