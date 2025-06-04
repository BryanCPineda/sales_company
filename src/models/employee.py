class Employee:
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
        return f"{self.__first_name} {self.__middle_initial}. {self.__last_name}"

    def get_tenure(self, current_date):
        return (current_date - self.__hire_date).days // 365

    def __repr__(self):
        return f"Employee({self.__employee_id}, {self.get_full_name()})"