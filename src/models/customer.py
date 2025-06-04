class Customer:
    def __init__(self, customer_id, first_name, middle_initial, last_name, city_id, address):
        self.__customer_id = customer_id
        self.__first_name = first_name
        self.__middle_initial = middle_initial
        self.__last_name = last_name
        self.__city_id = city_id
        self.__address = address

    def get_full_name(self):
        return f"{self.__first_name} {self.__middle_initial}. {self.__last_name}"

    def set_address(self, new_address):
        self.__address = new_address

    def __repr__(self):
        return f"Customer({self.__customer_id}, {self.get_full_name()}, {self.__address})"