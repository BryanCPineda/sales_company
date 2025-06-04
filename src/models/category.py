class Category:
    def __init__(self, category_id, category_name):
        self.__category_id = category_id
        self.__category_name = category_name

    def get_name(self):
        return self.__category_name

    def set_name(self, new_name):
        self.__category_name = new_name

    def __repr__(self):
        return f"Category({self.__category_id}, {self.__category_name})"