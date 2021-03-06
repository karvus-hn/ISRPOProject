from sqlalchemy import create_engine
from sqlalchemy import Table, Column
from sqlalchemy import MetaData, String, Integer, ForeignKey
#import sqlite3
 
#conn = sqlite3.connect("project.db")
engine = create_engine('sqlite:///project.db', echo = True)

metadata = MetaData()


restaurant = Table(
    'Restaurant', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('address', String),
    Column('phone', String),
    Column('coord', String),
    Column('image', String)
)

category = Table(
       'Category', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String))


dish = Table(
    'Dish', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('desc', String),
    Column('image', String),
    Column('category_id', Integer, ForeignKey('Category.id')),
)


menu_str = Table(
    'Menu_Str', metadata,
    Column('id', Integer, primary_key=True),
    Column('dish_id', Integer, ForeignKey('Dish.id')),
    Column('restaurant_id', Integer, ForeignKey('Restaurant.id')),
    Column('cost', Integer)
)


metadata.create_all(engine)