from typing import Text
from peewee import AutoField, TextField
import BaseModel



class TypesGoods(BaseModel):
    id = AutoField(column_name='id')
    type = TextField(column_name='type')

    class Meta:
        table_name = 'TypesGoods'

