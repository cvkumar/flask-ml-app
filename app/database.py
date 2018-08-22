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
    db.bind(provider='postgres', user=os.getenv('POSTGRES_USER'), password=os.getenv('POSTGRES_PASSWORD'),
            host=os.getenv('POSTGRES_HOST'), database=os.getenv('DATABASE'))

    db.generate_mapping(create_tables=True)
