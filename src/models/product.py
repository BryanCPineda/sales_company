class Product:
    def __init__(self, product_id, product_name, price, category_id, product_class, modify_date, resistant, is_allergic, vitality_days):
        self.__product_id = product_id
        self.__product_name = product_name
        self.__price = price
        self.__category_id = category_id
        self.__product_class = product_class
        self.__modify_date = modify_date
        self.__resistant = resistant
        self.__is_allergic = is_allergic
        self.__vitality_days = vitality_days

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        self.__price = new_price

    def __repr__(self):
        return f"Product({self.__product_id}, {self.__product_name}, ${self.__price})"