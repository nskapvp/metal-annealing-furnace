from fastapi import FastAPI
from typing import List
from sqlalchemy import create_engine, Column, Float, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

app = FastAPI()

# Создание соединения с базой данных PostgreSQL
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Dudkin2002@localhost/tagsdb"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Определение базового класса для моделей
Base = declarative_base()

# Определение модели для таблицы tags
class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    value = Column(Float)
    type = Column(String)

# Создание таблицы (если она еще не существует)
Base.metadata.create_all(bind=engine)

# Определение Pydantic модели для ответа
class TagResponse(BaseModel):
    id: int
    name: str
    value: float
    type: str

# Маршрут для чтения всех тегов из базы данных
@app.get("/api/tags", response_model=List[TagResponse])
async def read_tags():
    db = SessionLocal()
    tags = db.query(Tag).all()
    db.close()
    return tags

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=1888)
