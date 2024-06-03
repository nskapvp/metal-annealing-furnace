from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Параметры подключения к базе данных
DATABASE_URL = 'postgresql://postgres:Dudkin2002@127.0.0.1:5432/pechka'

# Создание двигателя и базового класса
engine = create_engine(DATABASE_URL)
Base = declarative_base()

# Создание сессии
Session = sessionmaker(bind=engine)
session = Session()
