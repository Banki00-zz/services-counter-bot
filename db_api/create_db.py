from sqlite3 import IntegrityError

from db_api.db import create_db
from services import RawService, AddService


def create_database():
    create_db()

