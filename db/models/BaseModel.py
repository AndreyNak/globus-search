from peewee import *
from models import connect

class BaseModel(Model):
    class Meta:
        database = connect