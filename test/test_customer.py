from src.models.customer import Customer

def test_get_full_name():
    """
    Test para verificar que get_full_name retorna el nombre completo correctamente formateado.
    """
    customer = Customer(1, "Ana", "L", "Pérez", 101, "Calle Falsa 123")
    assert customer.get_full_name() == "Ana L. Pérez"

def test_set_address():
    """
      Test para verificar que set_address actualiza la dirección correctamente.
    """
    customer = Customer(2, "Carlos", "M", "Gómez", 102, "Calle Vieja 456")
    customer.set_address("Nueva Dirección 789")
    assert customer._Customer__address == "Nueva Dirección 789"  

def test_customer_repr():
    """
      Test para verificar que el método __repr__ retorna la representación correcta del objeto Customer.
    """
    customer = Customer(3, "Luz", "S", "Martínez", 103, "San Martín 900")
    assert repr(customer) == "Customer(3, Luz S. Martínez, San Martín 900)"