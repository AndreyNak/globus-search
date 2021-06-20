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
        path_photo = f"photos/test/{path}"
        article = TypCategoryes(name=self.name_item,
                                path=path_photo,
                                name_type=type)
        article.save()



    def load_photo(self,message,bot):
        raw = message.document.file_id
        path = raw+".jpg"
        file_info = bot.get_file(raw)
        downloaded_file = bot.download_file(file_info.file_path)
        with open("photos/test/"+path,'wb') as new_file:
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