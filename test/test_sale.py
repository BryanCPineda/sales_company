from src.models.sale import Sale

def test_sale_init_and_get_total():
    """Verifica la inicialización y el método get_total."""
    venta = Sale(1, 100, 200, 300, 2, 0.10, 500.0, "10:00:00", "TX123")
    assert venta.get_total() == 500.0

def test_sale_apply_discount():
    """Verifica que el setter de descuento funcione correctamente."""
    venta = Sale(2, 101, 201, 301, 1, 0.0, 100.0, "11:00:00", "TX124")
    venta.apply_discount(0.25)
    assert venta._Sale__discount == 0.25  # Acceso directo solo para test, normalmente evitado en POO

def test_sale_repr():
    """Verifica la representación en cadena (__repr__)."""
    venta = Sale(3, 102, 202, 302, 3, 0.05, 1500.0, "09:30:00", "TX125")
    assert repr(venta) == "Sale(3, Product 302, $1500.0)"

def test_sale_private_attrs():
    """Verifica que los atributos privados existan."""
    venta = Sale(4, 103, 203, 303, 5, 0.2, 2500.0, "15:20:00", "TX126")
    assert hasattr(venta, "_Sale__sales_id")
    assert hasattr(venta, "_Sale__salesperson_id")
    assert hasattr(venta, "_Sale__customer_id")
    assert hasattr(venta, "_Sale__product_id")
    assert hasattr(venta, "_Sale__quantity")
    assert hasattr(venta, "_Sale__discount")
    assert hasattr(venta, "_Sale__total_price")
    assert hasattr(venta, "_Sale__sales_date")
    assert hasattr(venta, "_Sale__transaction_number")