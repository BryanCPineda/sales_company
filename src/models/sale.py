class Sale:
    def __init__(self, sales_id, salesperson_id, customer_id, product_id, quantity, discount, total_price, sales_date, transaction_number):
        self.__sales_id = sales_id
        self.__salesperson_id = salesperson_id
        self.__customer_id = customer_id
        self.__product_id = product_id
        self.__quantity = quantity
        self.__discount = discount
        self.__total_price = total_price
        self.__sales_date = sales_date
        self.__transaction_number = transaction_number

    def get_total(self):
        return self.__total_price

    def apply_discount(self, new_discount):
        self.__discount = new_discount

    def __repr__(self):
        return f"Sale({self.__sales_id}, Product {self.__product_id}, ${self.__total_price})"