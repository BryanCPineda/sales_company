from src.strategies.sales_by_branch_and_hour import SalesByBranchAndHourStrategy
from src.strategies.sales_customer_behavior import CustomerBehaviorStrategy
from src.strategies.sales_product_performance import ProductPerformanceStrategy

class ReportService:
    """
    Servicio centralizado para ejecutar y coordinar reportes estratégicos de ventas.
    Encapsula la lógica para ejecutar diferentes estrategias de análisis utilizando el patrón Facade.

    Permite a la capa de presentación acceder a los distintos análisis de negocio de forma simple y desacoplada.
    """
    def __init__(self, db):
        self.db = db

    def sales_by_branch_and_hour(self):
        """
        Genera un reporte de ventas agrupadas por sucursal (ciudad), hora y minuto.
        """
        strategy = SalesByBranchAndHourStrategy(self.db)
        return strategy.analyze()

    def customer_behavior(self):
        """
        Genera un reporte de análisis de comportamiento y patrones de gasto de los clientes.
        """
        strategy = CustomerBehaviorStrategy(self.db)
        return strategy.analyze()

    def product_performance(self, top_n=5):
        """
        Genera un reporte de rendimiento de productos por sucursal, mostrando los top N más vendidos.
        
        Args:
            top_n (int): Número de productos principales a incluir por sucursal.
        """
        strategy = ProductPerformanceStrategy(self.db, top_n=top_n)
        return strategy.analyze()