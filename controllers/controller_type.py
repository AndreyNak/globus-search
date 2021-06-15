from db.models.base_model import Types
import peewee

class ControllerTypeGoods:
    def __init__(self, name_type):
        self.name_type = name_type

    def add_item(self):
        article = Types(type=self.name_type)
        article.save()

    
    def delete_item(self):
        try:
            artist = Types.get(Types.type == self.name_type )
        except Exception:
            print('Не удален, потому что не найден !')
        else:
             artist.delete_instance()
             

    def update_item(self):
        artistId = Types.get(Types.type == self.name_type)
        new_word = input('На какое слово хочешь поменять ?')
        artist = Types(type=new_word)
        artist.id = artistId.id
        artist.save()