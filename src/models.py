import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    email = Column(String(20))
    name = Column(String(250), nullable=False, unique=False)
    surname = Column(String(250), nullable=False, unique=False)
    password = Column(String(250), nullable=False, unique=False)

class Favorites(Base):
    __tablename__ = 'Favorites'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer,ForeignKey("User.id"),primary_key=True)
    character_fav = Column(Integer,ForeignKey("Characters.id"), nullable=True)
    vehicle_fav = Column(Integer,ForeignKey("Vehicles.id"), nullable=True)
    planet_fav = Column(Integer,ForeignKey("Planets.id"), nullable=True)
    film_fav = Column(Integer,ForeignKey("Films.id"), nullable=True)
    rel= relationship(Characters)
    rel= relationship(Vehicles)
    rel= relationship(Planets)
    rel= relationship(Films)
  
class Characters(Base):
    __tablename__ = 'Characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    character_name = Column(String(250), unique=False, nullable=False)
    gender = Column(String(250), unique=False, nullable=False)
    hair_color = Column(String(250), unique=False, nullable=False)
    height = Column(Integer, unique=False, nullable=False)
    homeworld = Column(Integer, ForeignKey('Planets.id'))
    mass = Column(Integer, unique=False, nullable=False)
    skin_color = Column(String(250), unique=False, nullable=False)
    specie = Column(String(250), unique=False, nullable=False)

class Planets(Base):
    __tablename__ = 'Planets'
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(250), unique=False, nullable=False)
    climate = Column(String(250), nullable=False, unique=False)
    diameter = Column(Integer, nullable=False, unique=False)
    orbital_period = Column(Integer, nullable=False, unique=False)
    population = Column(Integer, nullable=False, unique=False)
    resident = Column(Integer, nullable=False, unique=False)
    rotation_period = Column(Integer, nullable=False, unique=False)
    surface_water = Column(Integer, nullable=False, unique=False)
    terrain = Column(String(250), nullable=False, unique=False)
    films = Column(Integer, ForeignKey('Films.id'))

class Films(Base):
    __tablename__ = 'Films'
    id = Column(Integer, primary_key=True)
    episode_name = Column(String(250), unique=False, nullable=False)
    created = Column(String(250), unique=False, nullable=False)
    director = Column(String(250), unique=False, nullable=False)
    edited = Column(String(250), unique=False, nullable=False)
    opening_crawl = Column(String(250), unique=False, nullable=False)

class Vehicles(Base):
    __tablename__ = 'Vehicles'
    id = Column(Integer, primary_key=True)
    vehicle_name = Column(String(250), unique=False, nullable=False)
    model = Column(String(250), nullable=False, unique=False)
    manufacturer = Column(String(250), nullable=False, unique=False)
    cargo_capacity = Column(Integer, nullable=False, unique=False)
    consumables = Column(String(250), nullable=False, unique=False)
    cost_in_credits = Column(Integer, nullable=False, unique=False)
    created = Column(String(250), nullable=False, unique=False)
    crew = Column(Integer, nullable=False, unique=False)
    edited = Column(String(250),  nullable=False, unique=False)
    lenght = Column(Integer, nullable=False, unique=False)
    max_atmosphering_speed = Column(Integer, nullable=False, unique=False)
    passengers = Column(Integer, nullable=False, unique=False)
    pilots = Column(Integer, nullable=False, unique=False)
    films = Column(Integer, ForeignKey('Films.id'))

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
