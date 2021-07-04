from os import path
import requests
import telebot
from db.models.categoryes_model import TypCategoryes
from db.models.types_model import Types
from controllers.controller_type import ControllerTypeGoods
from controllers.controller_categories import ControllerCategories
from db.connect import *
import time
from pyaspeller import YandexSpeller



#my_request = input(":")



def speller_filter(message):
    speller = YandexSpeller()
    fixed = speller.spelled(message)
    if (message != fixed):
        return fixed
    return message


# str = speller_filter(my_request)
# print(str)

