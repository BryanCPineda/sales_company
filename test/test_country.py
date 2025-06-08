from src.models.country import Country

def test_country_init_and_get_code():
    """Verifica la inicialización y el acceso al código del país."""
    country = Country(1, "Argentina", "AR")
    assert country.get_code() == "AR"

def test_country_str():
    """Verifica la representación en cadena (__str__)."""
    country = Country(2, "Bolivia", "BO")
    assert str(country) == "Country(Bolivia, BO)"

def test_country_private_attrs():
    """Verifica que los atributos privados existan."""
    country = Country(3, "Chile", "CL")
    assert hasattr(country, "_Country__country_id")
    assert hasattr(country, "_Country__country_name")
    assert hasattr(country, "_Country__country_code")