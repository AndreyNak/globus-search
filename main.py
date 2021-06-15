from controllers.controller_type import ControllerTypeGoods
from db.connect import *



conn = Con.connect()
Con.m_cursor(conn)
question = input('Хотите добавить тип товара ? ')
if question == 'да':
    obg = ControllerTypeGoods(input('Название типа: '))
    obg.add_item()
else:
    print('пока!')
    exit()
    

conn.close()



# def connect():
#     conn = 'db/globus_database.db'
#     if os.path.isfile(conn):
#         print('good')
#         return SqliteDatabase(conn)
#     else:
#         print('bad')
#         exit()

# def m_cursor(conn):
#     return conn.cursor()

# class BaseModel(Model):
#     class Meta:
#         database = connect()


# class TypesGoods(BaseModel):
#     id = AutoField(column_name='id')
#     type = TextField(column_name='type')

#     class Meta:
#         table_name = 'TypesGoods'


# article = TypesGoods(type='Алкоголь')
# cursor = m_cursor(connect())
# article.save()


# class ControllerTypeGoods:
#     def __init__(self, name_type):
#         self.name_type = name_type

#     def add_item(self):
#         article = TypesGoods(type=self.name_type)
#         article.save()

# obg = ControllerTypeGoods('Алкоголь')
# obg.add_item()


# question = input('Хотите добавить тип товара ? ')
# if question == 'да':
#     obg = ControllerTypeGoods(input('Название типа'))
#     obg.add_item()
# else:
#     exit()
