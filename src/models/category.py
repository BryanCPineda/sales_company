class Category:
    """
    Representa una categoría en el sistema.
    Atributos:
        category_id (int): Identificador único de la categoría.
        category_name (str): Nombre de la categoría.
    """
    def __init__(self, category_id, category_name):
        self.__category_id = category_id
        self.__category_name = category_name

    def get_name(self):
        """        
        Obtiene el nombre de la categoría.
        Returns:
            str: Nombre de la categoría.
        """
        return self.__category_name

    def set_name(self, new_name):
        """        
        Establece un nuevo nombre para la categoría.
        Args:
            new_name (str): Nuevo nombre de la categoría.
        """
        self.__category_name = new_name

    def __repr__(self):
        """ 
        Representación en cadena de la categoría.
        Returns:
            str: Representación de la categoría.
        """
        return f"Category({self.__category_id}, {self.__category_name})"