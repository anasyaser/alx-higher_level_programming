#!/usr/bin/python3
"""
Connect to datebase and create cities table
city table : id(primary key), name(city name), state_id(foreign key)
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class City(Base):
    """Declartive Calss to City Table"""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, ForeignKey('states.id'))

    state = relationship("State", back_populates="cities")
