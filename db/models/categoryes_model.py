from peewee import *
from db.models.base_model import BaseModel


class TypCategoryes(BaseModel):
    id = AutoField(column_name='id')
    name = TextField(column_name='name')
    path = TextField(column_name='path')
    name_type = TextField(column_name='name_type', null=True)
    
    class Meta:
        table_name = 'Category'