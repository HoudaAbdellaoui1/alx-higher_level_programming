#!/usr/bin/python3
"""First state model"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False,
                unique=True)
    name = Column(String(128), nullable=False)

engine = create_engine('mysql://username:password@localhost:3306/database_name')
Base.metadata.create_all(engine)
