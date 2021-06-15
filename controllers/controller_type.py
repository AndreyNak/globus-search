from db.models.base_model import Types


class ControllerTypeGoods:
    def __init__(self, name_type):
        self.name_type = name_type

    def add_item(self):
        article = Types(type=self.name_type)
        article.save()