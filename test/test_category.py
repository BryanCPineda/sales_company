from src.models.category import Category

def test_category_init_and_getters():
    """Verifica la correcta inicialización y acceso a los atributos privados."""
    category = Category(1, "Bebidas")
    assert category.get_name() == "Bebidas"

def test_category_set_name():
    """Verifica el setter para el nombre de la categoría."""
    category = Category(2, "Snacks")
    category.set_name("Galletas")
    assert category.get_name() == "Galletas"

def test_category_repr():
    """Verifica la representación en cadena (__repr__)."""
    category = Category(3, "Lácteos")
    assert repr(category) == "Category(3, Lácteos)"