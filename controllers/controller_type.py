from db.models.base_model import Types
import peewee
import os


class ControllerTypeGoods:
    def __init__(self, name_type=None):
        self.name_type = name_type
    
    def select_items(self):
        cur_query = Types.select()
        return [i['type'] for i in cur_query.dicts().execute()]       
        

    def show_item(self):
        item = Types.get(Types.type == self.name_type)
        return item.path

    def add_item(self,path):
        path_photo = f"photos/{path}"
        article = Types(type=self.name_type,path=path_photo)
        article.save()

    
    def delete_item(self):
        try:
            artist = Types.get(Types.type == self.name_type )
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
