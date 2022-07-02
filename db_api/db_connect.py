import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy_utils import database_exists, create_database

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

url_engine = create_engine("postgresql://bktydisjihcptq:883d49998ea5baaaf53d54c484cfe343f7d28c09f0fc59e1ad1c408424069577@ec2-99-81-137-11.eu-west-1.compute.amazonaws.com:5432/dbr0nlg8cp8nbk")


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
