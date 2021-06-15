from db.models.base_model import Types
import peewee

class ControllerTypeGoods:
    def __init__(self, name_type=None):
        self.name_type = name_type

    def show_items(self):
        cur_query = Types.select().limit(5).order_by(Types.id.desc())
        n = 1
        for i in cur_query.dicts().execute():
            print(f"{n} {i['type']}")
            n+=1
        
                

    def add_item(self):
        article = Types(type=self.name_type)
        article.save()

    
    def delete_item(self):
        try:
            artist = Types.get(Types.type == self.name_type )
        except Exception:
            return 'Не удален, потому что не найден !'
        else:
             artist.delete_instance()
             return 'Экземпляр был успешно удален !'

    # def update_search_item(self):
    #     artistId = Types.get(Types.type == self.name_type)
    #     new_word = input('На какое слово хочешь поменять ?')
    #     artist = Types(type=new_word)
    #     artist.id = artistId.id
    #     artist.save()