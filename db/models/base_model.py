from peewee import *
from db.connect import *


class BaseModel(Model):
    class Meta:
        database = Con.connect()


class Types(BaseModel):
    id = AutoField(column_name='id')
    type = TextField(column_name='type', null=True)

    class Meta:
        table_name = 'Types'