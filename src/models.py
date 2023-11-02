import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    email = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False, unique=False)
    surname = Column(String(250), nullable=False, unique=False)
    password = Column(String(250), nullable=False, unique=False)
    date_of_bird = Column(String(250), nullable=False, unique=False)

class Film(Base):
    __tablename__ = 'film'
    episode_id = Column(Integer, primary_key=True)
    created = Column(String(250), unique=False, nullable=False)
    director = Column(String(250), unique=False, nullable=False)
    edited = Column(String(250), unique=False, nullable=False)
    opening_crawl = Column(String(250), unique=False, nullable=False)

class Planet(Base):
    __tablename__ = 'planet'
    name = Column(String(250), primary_key=True)
    climate = Column(String(250), nullable=False, unique=False)
    diameter = Column(Integer, nullable=False, unique=False)
    films = Column(String(250), ForeignKey('film.episode_id'))
    orbital_period = Column(Integer, nullable=False, unique=False)
    population = Column(Integer, nullable=False, unique=False)
    resident = Column(Integer, nullable=False, unique=False)
    rotation_period = Column(Integer, nullable=False, unique=False)
    surface_water = Column(Integer, nullable=False, unique=False)
    terrain = Column(String(250), nullable=False, unique=False)

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    name = Column(String(250), primary_key=True)
    gender = Column(String(250), unique=False, nullable=False)
    hair_color = Column(String(250), unique=False, nullable=False)
    height = Column(Integer, unique=False, nullable=False)
    homeworld = Column(String(250),ForeignKey('planet.name'))
    mass = Column(Integer, unique=False, nullable=False)
    skin_color = Column(String(250), unique=False, nullable=False)
    specie = Column(String(250), unique=False, nullable=False)

class Vehicle(Base):
    __tablename__ = 'vehicle'
    name = Column(String(250), primary_key=True)
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
    films = Column(String(250), ForeignKey('film.episode_id'))

class Fav_character_user(Base):
    __tablename__ ='fav_character_user'
    name = Column(String(250), primary_key=True)
    email = Column(String(250),ForeignKey('user.email'))
    Fav_character_character = Column(String(30),ForeignKey('character.name'))
    rel_character = relationship('Character')
    rel_user = relationship('User')

class Fav_vehicles_user(Base):
    __tablename__ ='fav_vehicles_user'
    name = Column(String(250), primary_key=True)
    email = Column(String(250), ForeignKey('user.email'))
    Fav_vehicles_vehicles = Column(String(30),ForeignKey('vehicle.name'))
    rel_character = relationship('Vehicle')
    rel_user = relationship('User')


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
