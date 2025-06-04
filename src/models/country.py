class Country:
    def __init__(self, country_id, country_name, country_code):
        self.__country_id = country_id
        self.__country_name = country_name
        self.__country_code = country_code

    def get_code(self):
        return self.__country_code

    def __str__(self):
        return f"Country({self.__country_name}, {self.__country_code})"