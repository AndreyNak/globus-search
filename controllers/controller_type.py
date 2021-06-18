import re

from telebot.types import ReplyKeyboardMarkup
from db.models.base_model import Types,TypCategoryes
import peewee
import os


class ControllerTypeGoods:
    def __init__(self, name_type=None):
        self.name_item = name_type
    
    def select_items(self):
        cur_query = Types.select()
        return [i['type']for i in cur_query.dicts().execute()]

    def show_type(self):
        return Types.get(Types.type == self.name_item)
       

    def add_item(self,path, side):
        path_photo = f"photos/{path}"
        article = Types(type=self.name_item,path=path_photo, side=side)
        article.save()

    
    def delete_item(self):
        try:
            artist = Types.get(Types.type == self.name_item )
        except Exception:
            return 'Не удален, потому что не найден !'
        else:
            os.remove(f"{artist.path}")
            artist.delete_instance()

#     def update_item(self):
#         artistId = Types.get(Types.type == self.name_type)
#         new_word = input('На какое слово хочешь поменять ?')
#         artist = Types(type=new_word)
#         artist.id = artistId.id
#         artist.save()