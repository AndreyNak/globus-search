
from peewee import *
from db.connect import *


class BaseModel(Model):
    class Meta:
        database = Con.connect()



# class Types(BaseModel):
#     id = AutoField(column_name='id')
#     type = TextField(column_name='type')
#     path = TextField(column_name='path')
#     side = TextField(column_name='side')

#     class Meta:
#         table_name = 'Types'




# class TypCategoryes(BaseModel):
#     id = AutoField(column_name='id')
#     name = TextField(column_name='name')
#     path = TextField(column_name='path')
#     name_type = TextField(column_name='name_type', null=True)
    
#     class Meta:
#         table_name = 'Category'