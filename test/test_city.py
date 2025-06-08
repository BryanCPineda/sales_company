from src.models.city import City

def test_city_init_and_getters():
    """Verifica la inicialización y acceso a los atributos públicos."""
    city = City(10, "Jujuy", "4600", 1)
    assert city.get_name() == "Jujuy"
    assert city.get_country_id() == 1

def test_city_repr():
    """Verifica la representación en cadena (__repr__)."""
    city = City(20, "Salta", "4400", 2)
    assert repr(city) == "City(20, Salta, 4400)"

def test_city_private_attrs():
    """Verifica que los atributos privados existan."""
    city = City(30, "Tucumán", "4000", 3)
    assert hasattr(city, "_City__city_id")
    assert hasattr(city, "_City__city_name")
    assert hasattr(city, "_City__zipcode")
    assert hasattr(city, "_City__country_id")