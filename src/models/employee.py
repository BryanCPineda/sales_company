class Employee:
    """
    Representa un empleado en el sistema. 
    Atributos:
        employee_id (int): Identificador único del empleado.
        first_name (str): Nombre del empleado.
        middle_initial (str): Inicial del segundo nombre del empleado.
        last_name (str): Apellido del empleado.
        birth_date (date): Fecha de nacimiento del empleado.
    """
    def __init__(self, employee_id, first_name, middle_initial, last_name, birth_date, gender, city_id, hire_date):
        self.__employee_id = employee_id
        self.__first_name = first_name
        self.__middle_initial = middle_initial
        self.__last_name = last_name
        self.__birth_date = birth_date
        self.__gender = gender
        self.__city_id = city_id
        self.__hire_date = hire_date

    def get_full_name(self):
        """
        Obtiene el nombre completo del empleado.
        Returns:
            str: Nombre completo del empleado en formato "Nombre M. Apellido".
        """
        return f"{self.__first_name} {self.__middle_initial}. {self.__last_name}"

    def get_tenure(self, current_date):
        """
        Calcula el tiempo de servicio del empleado en años.
        Args:
            current_date (date): Fecha actual para calcular el tiempo de servicio.  
        Returns:
            int: Número de años que el empleado ha estado en servicio.
        """
        return (current_date - self.__hire_date).days // 365

    def __repr__(self):
        """
        Representación en cadena del empleado.
        Returns:
            str: Representación del empleado con su ID y nombre completo.
        """
        return f"Employee({self.__employee_id}, {self.get_full_name()})"