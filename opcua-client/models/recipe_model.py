from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from controller.db_driver import Base

class Stage(Base):
    __tablename__ = 'stage'
    id = Column(Integer, primary_key=True)
    time_ustavka = Column(Float, nullable=False)
    temperature_ustavka = Column(Float, nullable=False)
    gas = Column(Float, nullable=False)
    pressure = Column(Float, nullable=False)

class Recipe(Base):
    __tablename__ = 'recipe'
    id = Column(Integer, primary_key=True)
    name_recipe = Column(String(30), nullable=False)
    stage_1_id = Column(Integer, ForeignKey('stage.id'), nullable=False)
    stage_2_id = Column(Integer, ForeignKey('stage.id'), nullable=False)
    stage_3_id = Column(Integer, ForeignKey('stage.id'), nullable=False)
    stage_4_id = Column(Integer, ForeignKey('stage.id'), nullable=False)
    stage_5_id = Column(Integer, ForeignKey('stage.id'), nullable=False)

    stage_1 = relationship("Stage", foreign_keys=[stage_1_id])
    stage_2 = relationship("Stage", foreign_keys=[stage_2_id])
    stage_3 = relationship("Stage", foreign_keys=[stage_3_id])
    stage_4 = relationship("Stage", foreign_keys=[stage_4_id])
    stage_5 = relationship("Stage", foreign_keys=[stage_5_id])


