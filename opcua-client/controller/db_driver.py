from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import configparser
from sqlalchemy.exc import OperationalError


config = configparser.ConfigParser()
config.read('C:\\trash\\University\\DIPLOM\\metal-annealing-furnace\\opcua-client\\controller\\db_config.ini')
config.sections()
DATABASE_USER = config.get('database', 'user')
DATABASE_PASSWORD = config.get('database', 'password')
DATABASE_HOST = config.get('database', 'host')
DATABASE_PORT = config.get('database', 'port')
DATABASE_NAME = config.get('database', 'dbname')

DATABASE_URL = f'postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}'

try:
    engine = create_engine(DATABASE_URL)
    Base = declarative_base()
    Session = sessionmaker(bind=engine)
    session = Session()
    print("Подключение к базе данных успешно!")
except OperationalError as e:
    print(f"Ошибка подключения к базе данных: {e}")
