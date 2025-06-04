class Country:
    """
    Representa una país en el sistema.
    Atributos: 
        country_id (int): Identificador único del país.
        country_name (str): Nombre del país.
        country_code (str): Código ISO del país.
    """
    def __init__(self, country_id, country_name, country_code):
        self.__country_id = country_id
        self.__country_name = country_name
        self.__country_code = country_code

    def get_code(self):
        """
        Obtiene el código ISO del país.
        Returns:
            str: Código ISO del país.
        """
        return self.__country_code

    def __str__(self):
        """
        Representación en cadena del país.
        Returns:
            str: Nombre del país.
        """
        return f"Country({self.__country_name}, {self.__country_code})"