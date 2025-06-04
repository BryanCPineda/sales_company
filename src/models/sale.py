class Sale:
    """
    Representa una venta en el sistema.
    Atributos:
        sales_id (int): Identificador único de la venta.
        salesperson_id (int): Identificador del vendedor que realizó la venta.
        customer_id (int): Identificador del cliente al que se le realizó la venta.
        product_id (int): Identificador del producto vendido.
        quantity (int): Cantidad de productos vendidos.
        discount (float): Descuento aplicado a la venta.
        total_price (float): Precio total de la venta.
        sales_date (str): Fecha en que se realizó la venta.
        transaction_number (str): Número de transacción asociado a la venta.
    """
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
        """
        Obtiene el precio total de la venta, aplicando el descuento si es necesario.
        Returns:
            float: Precio total de la venta.
        """
        return self.__total_price

    def apply_discount(self, new_discount):
        """
        Aplica un nuevo descuento a la venta.
        Args:
            new_discount (float): Nuevo descuento a aplicar.
        """
        self.__discount = new_discount

    def __repr__(self):
        """
        Representación en cadena de la venta.
        Returns:
            str: Representación de la venta con su ID, producto y precio total.
        """
        return f"Sale({self.__sales_id}, Product {self.__product_id}, ${self.__total_price})"