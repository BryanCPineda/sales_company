class Product:
    """
    Represeta un producto en el sistema.
    Atributos:
        product_id (int): Identificador único del producto.
        product_name (str): Nombre del producto.
        price (float): Precio del producto.
        category_id (int): Identificador de la categoría a la que pertenece el producto.
        product_class (str): Clase del producto (por ejemplo, "alimento", "medicamento").
        modify_date (str): Fecha de la última modificación del producto.
        resistant (bool): Indica si el producto es resistente a enfermedades.
        is_allergic (bool): Indica si el producto es alérgico.
        vitality_days (int): Días de vitalidad del producto.
    """
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
        """
        Obtiene el precio del producto.
        Returns:
            float: Precio del producto.
        """
        return self.__price

    def set_price(self, new_price):
        """
        Establece un nuevo precio para el producto.
        Args:
            new_price (float): Nuevo precio del producto.
        """
        self.__price = new_price

    def __repr__(self):
        """
        Representación en cadena del producto.
        Returns:
            str: Representación del producto con su ID, nombre y precio.
        """
        return f"Product({self.__product_id}, {self.__product_name}, ${self.__price})"