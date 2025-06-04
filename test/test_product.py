from src.models.product import Product

def test_get_price():
    product = Product(1, "Leche", 3.50, 1, "A", "12:00", "Sí", "No", 7)
    assert product.get_price() == 3.50

def test_set_price():
    product = Product(2, "Pan", 2.00, 1, "B", "13:00", "No", "No", 2)
    product.set_price(2.50)
    assert product.get_price() == 2.50

def test_product_repr():
    product = Product(3, "Queso", 4.75, 2, "C", "14:00", "Sí", "Sí", 10)
    assert repr(product) == "Product(3, Queso, $4.75)"