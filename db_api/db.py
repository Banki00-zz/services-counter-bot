import logging

from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker, declarative_base
from config import *

logger = logging.getLogger('logger')

DATABASE = {
    'drivername': 'postgres',  # Тут можно использовать MySQL или другой драйвер
    'host': f'{HOST}',
    'port': '5432',
    'username': f'{DB_USERNAME}',
    'password': f'{DB_PASSWORD}',
    'database': f'{DATABASE}'
}

Base = declarative_base()

# Создаем объект Engine, который будет использоваться объектами ниже для связи с БД
# engine = create_engine(URL(**DATABASE))
engine = create_engine("postgresql://bktydisjihcptq:883d49998ea5baaaf53d54c484cfe343f7d28c09f0fc59e1ad1c408424069577@ec2-99-81-137-11.eu-west-1.compute.amazonaws.com:5432/dbr0nlg8cp8nbk")
# Метод create_all создает таблицы в БД , определенные с помощью  DeclarativeBase
Base.metadata.create_all(engine)
# Создаем фабрику для создания экземпляров Session. Для создания фабрики в аргументе
# bind передаем объект engine
session = sessionmaker(bind=engine)
# Создаем объект сессии из вышесозданной фабрики Session

