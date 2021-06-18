from telebot.types import ReplyKeyboardMarkup
from db.models.base_model import Types,TypCategoryes
import peewee
import os


class ControllerCategories:
    def __init__(self, name_type=None):
        self.name_item = name_type
    

    def select_items1(self):
        cur_query = TypCategoryes.select()
        return [i['name']for i in cur_query.dicts().execute()]


    def select_category(self):
        return TypCategoryes.get(TypCategoryes.name == self.name_item)
       
       
    def add_category_item(self,path,type):
        path_photo = f"photos/category/{path}"
        article = TypCategoryes(name=self.name_item,path=path_photo,name_type=type)
        article.save()