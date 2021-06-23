import re
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
        try:
            return TypCategoryes.get(TypCategoryes.name == self.name_item)
        except Exception:
            return False
       


    def select_select_category(self):
        return TypCategoryes.get(TypCategoryes.name == self.name_item)

        


    def add_category_item(self,path,type):
        path_photo = f"photos/category/{path}"
        if (self.select_category()):
            print(f"[ {self.name_item} : уже есть в базе ! ]")
        else:
            article = TypCategoryes(name=self.name_item,
                                    path=path_photo,
                                    name_type=type)
            article.save()
            print('\nЭлемент Добавлен !\n')


    def load_photo(self,message,bot):
        raw = message.document.file_id
        path = raw+".png"
        file_info = bot.get_file(raw)
        downloaded_file = bot.download_file(file_info.file_path)
        with open("photos/category/"+path,'wb') as new_file:
            new_file.write(downloaded_file)
        return path


    def delete_item(self):
        try:
            artist = self.select_category()
        except Exception:
            return 'Не удален, потому что не найден !'
        else:
            os.remove(f"{artist.path}")
            artist.delete_instance()