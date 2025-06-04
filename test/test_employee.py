from src.models.employee import Employee
from datetime import date

def test_employee_full_name():
    """
      Test para verificar que get_full_name retorna el nombre completo correctamente formateado.
    """
    employee = Employee(1, "Juan", "A", "Rodríguez", date(1990, 5, 1), "M", 200, date(2015, 4, 10))
    assert employee.get_full_name() == "Juan A. Rodríguez"

def test_employee_tenure():
    """
      Test para verificar que get_tenure calcula correctamente el tiempo de servicio del empleado.
    """
    employee = Employee(2, "Laura", "M", "Gómez", date(1992, 7, 10), "F", 201, date(2020, 3, 1))
    assert employee.get_tenure(date(2024, 3, 1)) == 4 