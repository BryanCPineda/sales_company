class Customer:
    """
    Representa un cliente en el sistema.
    Atributos:
        customer_id (int): Identificador único del cliente.
        first_name (str): Nombre del cliente.
        middle_initial (str): Inicial del segundo nombre del cliente.
        last_name (str): Apellido del cliente.
        city_id (int): Identificador de la ciudad donde reside el cliente.
        address (str): Dirección del cliente.
    """
    def __init__(self, customer_id, first_name, middle_initial, last_name, city_id, address):
        self.__customer_id = customer_id
        self.__first_name = first_name
        self.__middle_initial = middle_initial
        self.__last_name = last_name
        self.__city_id = city_id
        self.__address = address

    def get_full_name(self):
        """
        Obtiene el nombre completo del cliente.
        Returns:
            str: Nombre completo del cliente en formato "Nombre M. Apellido".
        """
        return f"{self.__first_name} {self.__middle_initial}. {self.__last_name}"

    def set_address(self, new_address):
        """
        Establece una nueva dirección para el cliente.
        Args:
            new_address (str): Nueva dirección del cliente.
        """
        self.__address = new_address

    def __repr__(self):
        """
        Representación en cadena del cliente.
        Returns:
            str: Representación del cliente con su ID, nombre completo y dirección.
        """
        return f"Customer({self.__customer_id}, {self.get_full_name()}, {self.__address})"