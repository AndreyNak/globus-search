from controllers.controller_type import ControllerTypeGoods
from db.connect import *




def update():
    #--------------------Изменение--------------------
    obg = ControllerTypeGoods(input('Название типа которое хочешь поменять: '))
    obg.update_item()
    #--------------------Изменение--------------------


