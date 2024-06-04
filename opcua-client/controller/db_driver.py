from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import getpass

password  = getpass.getpass('Введи пароль от БД: ')
print(f"Пароль длиной {len(password)} символов успешно введен.")

DATABASE_URL = f'postgresql://postgres:{password}@127.0.0.1:5432/pechka'

engine = create_engine(DATABASE_URL)
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()
