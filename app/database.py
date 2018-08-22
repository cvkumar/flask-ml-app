from pony.orm import *
from datetime import datetime
import os

db = Database()


class Prediction(db.Entity):
    id = PrimaryKey(unicode)
    date = Required(datetime)
    sepal_length = Required(float)
    sepal_width = Required(float)
    petal_length = Required(float)
    petal_width = Required(float)
    prediction = Required(str)


def connect_database():
    db.bind(provider='postgres', user=os.environ['POSTGRES_USER'], password=os.environ['POSTGRES_PASSWORD'],
            host="postgres", database=os.environ['POSTGRES_DB'], port=5432)
    db.generate_mapping(create_tables=True)
