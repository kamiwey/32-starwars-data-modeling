import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

class User(Base):
    __tablename__= 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(120), nullable=False)
    email = Column(String(250), nullable=False)
    Password =Column (Integer)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    population = Column(String(50), nullable=False)
    rotation_period = Column(String(20), nullable=False)
    surface_water = Column(String(20), nullable=False)
    gravity = Column(String(20), nullable=False)
    climate = Column(String(20), nullable=False)
    
class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)    
    name = Column(String(50), nullable=False)
    birth_year = Column(String(50), nullable=False)
    gender = Column(String(20), nullable=False)
    height = Column(String(20),  nullable=False)
    skin_color = Column(String(20), nullable=False)
    eye_color = Column(String(20), nullable=False)
    planets_id = Column(Integer, ForeignKey('planets.id'))
    planets = relationship(Planets)



class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    model = Column(String(80), nullable=False)
    manufacturer = Column(String(80), nullable=False)
    passengers = Column(String(20), nullable=False)
    cargo_capacity = Column(String(80), nullable=False)
    vehicle_class = Column(String(80), nullable=False)
    

class FavoritePeople(Base):
    __tablename__ = 'favoritePeople'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    people_id = Column(Integer, ForeignKey('people.id'))
    user = relationship(User)
    people = relationship(People)

class FavoritePlanets(Base):
    __tablename__ = 'favoritePlanets'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planets_id = Column(Integer, ForeignKey('planets.id'))
    user = relationship(User)
    planets = relationship(Planets)

class FavoriteVehicles(Base):
    __tablename__ = 'favoriteVehicles'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    vehicles_id = Column(Integer, ForeignKey('vehicles.id'))
    user = relationship(User)
    vehicles = relationship(Vehicles)
    
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
