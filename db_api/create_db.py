import os.path
from sqlalchemy_utils import database_exists

import services as db_creator
from db_api.db_connect import url_engine

if __name__ == '__main__':
    if database_exists(url_engine):
        db_creator.create_database()
