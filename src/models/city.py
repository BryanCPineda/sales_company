class City:
    """
    Representa una ciudad en el sistema.
    Atributos: 
        city_id (int): Identificador único de la ciudad.
        city_name (str): Nombre de la ciudad.
        zipcode (str): Código postal de la ciudad.
        country_id (int): Identificador del país al que pertenece la ciudad.
    """
    def __init__(self, city_id, city_name, zipcode, country_id):
        self.__city_id = city_id
        self.__city_name = city_name
        self.__zipcode = zipcode
        self.__country_id = country_id

    def get_name(self):
        """
        Obtiene el nombre de la ciudad.
        Returns:
            str: Nombre de la ciudad.
        """
        return self.__city_name

    def get_country_id(self):
        """ 
        Obtiene el identificador del país al que pertenece la ciudad.
        Returns:
            int: Identificador del país.
        """
        return self.__country_id

    def __repr__(self):
        """
        Representación en cadena de la ciudad.
        Returns:
            str: Representación de la ciudad.
        """
        return f"City({self.__city_id}, {self.__city_name}, {self.__zipcode})"