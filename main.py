from copy import Error
from logging import error
from controllers.controller_type import ControllerTypeGoods
from db.connect import *

conn = Con.connect()
Con.m_cursor(conn)

#--------------------Добавление--------------------
# question = input('Хотите добавить тип товара ? ')
# if question == 'да':
#     obg = ControllerTypeGoods(input('Название типа: '))
#     obg.add_item()
# else:
#     print('пока!')
#     exit()
#--------------------Добавление--------------------

#--------------------Изменение--------------------
# obg = ControllerTypeGoods(input('Название типа которое хочешь поменять: '))
# obg.update_item()
#--------------------Изменение--------------------


#--------------------Удаление--------------------
# question = input('Хотите удалить тип товара ? ')
# if question == 'да':
#     obg = ControllerTypeGoods(input('Название типа: '))
#     obg.delete_item()   
# else:
#     print('пока!')
#     exit() 
#--------------------Удаление--------------------
conn.close()

