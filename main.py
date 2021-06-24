import telebot
from db.models.categoryes_model import TypCategoryes
from db.models.types_model import Types
from controllers.controller_type import ControllerTypeGoods
from controllers.controller_categories import ControllerCategories
from db.connect import *




# message = input("Слово:")






# def show_what_have(message):
#     obg = ControllerCategories()
#     return [i for i in obg.select_items1() if i.find(message)!= - 1]


# print(f"Ничего не найдено, может вы имели ввиду: {show_what_have(message)}")