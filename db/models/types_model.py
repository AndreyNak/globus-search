
from peewee import *
from db.models.base_model import BaseModel


class Types(BaseModel):
    id = AutoField(column_name='id')
    type = TextField(column_name='type')
    path = TextField(column_name='path')
    side = TextField(column_name='side')

    class Meta:
        table_name = 'Types'