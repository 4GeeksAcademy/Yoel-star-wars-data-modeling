from eralchemy2 import render_er

from sqlalchemy import Column
from sqlalchemy import Table
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String, Integer, Float, Boolean
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass

association_table = Table('association', Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id'), primary_key=True),
    Column('planet_id', Integer, ForeignKey('planet.id'), nullable=True, primary_key=True),
    Column('character_id', Integer, ForeignKey('character.id'), nullable=True, primary_key=True)
)

class User(Base):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    username: Mapped[str]  = mapped_column(unique=True, nullable=False)
    name: Mapped[str]
    last_name: Mapped[str] = mapped_column(nullable=True)
    email: Mapped[str] 
    country: Mapped[str] = mapped_column(nullable=True)
    planets: Mapped[List["Planet"]] = relationship(secondary=association_table, back_populates='users')
    characters: Mapped[List["Character"]] = relationship(secondary=association_table, back_populates='users')

class Planet(Base):
    __tablename__ = 'planet'
    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    name: Mapped[str] 
    population: Mapped[int] = mapped_column(nullable=True)
    gravity: Mapped[int] = mapped_column(nullable=True)
    climate: Mapped[str] = mapped_column(nullable=True)
    users: Mapped[List["User"]] = relationship(secondary=association_table, back_populates='planets')
   

class Character(Base):
    __tablename__ = 'character'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, unique=True)
    name: Mapped[str] 
    last_name: Mapped[str] = mapped_column(nullable=True)
    eye_color: Mapped[str] = mapped_column(nullable=True)
    height: Mapped[int] = mapped_column(nullable=True)
    origin_planet: Mapped[str] = mapped_column(nullable=True)
    users: Mapped[List["User"]] = relationship(secondary=association_table, back_populates='characters')
    


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
