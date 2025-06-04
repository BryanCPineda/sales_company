class City:
    def __init__(self, city_id, city_name, zipcode, country_id):
        self.__city_id = city_id
        self.__city_name = city_name
        self.__zipcode = zipcode
        self.__country_id = country_id

    def get_name(self):
        return self.__city_name

    def get_country_id(self):
        return self.__country_id

    def __repr__(self):
        return f"City({self.__city_id}, {self.__city_name}, {self.__zipcode})"