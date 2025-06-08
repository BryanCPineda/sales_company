from src.strategies.sales_analysis_strategy import SalesAnalysisStrategy
import pandas as pd
import time

class CustomerBehaviorStrategy(SalesAnalysisStrategy):
    """
    Estrategia de análisis de patrones de comportamiento de los clientes.

    Esta estrategia utiliza CTE y funciones ventana (ROW_NUMBER) para obtener:
    - El total gastado, cantidad de transacciones y desglose de gasto con/sin promoción para cada cliente.
    - La sucursal donde el cliente gastó más (ciudad de mayor gasto).
    - El producto más comprado por cada cliente.

    Returns:
        pd.DataFrame: DataFrame con las columnas
            ['CustomerID', 'cliente', 'total_gastado', 'transacciones', 
            'gastado_con_promocion', 'gastado_sin_promocion', 
            'sucursal_donde_mas_gasto', 'producto_mas_comprado'],
            ordenado por gasto total descendente.
    """
    def __init__(self, db):
        self.db = db

    def analyze(self) -> pd.DataFrame:
        query = """SELECT * FROM vw_customer_behavior"""
        start = time.time()
        df = self.db.execute_query_as_dataframe(query)
        end = time.time()
        
        print(f"Tiempo de ejecución: {end - start:.3f} segundos")
        print("🔹 Top clientes por gasto y aprovechamiento de promociones:")
        return df