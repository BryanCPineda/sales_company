from src.strategies.sales_analysis_strategy import SalesAnalysisStrategy
import pandas as pd
import time

class SalesByBranchAndHourStrategy(SalesAnalysisStrategy):
    """
    Estrategia de análisis que identifica, para cada sucursal, hora y minuto, 
    el producto más vendido y el descuento aplicado.

    Utiliza una consulta SQL avanzada con CTE y función ventana (ROW_NUMBER)
    para agrupar las ventas y seleccionar el producto con mayor cantidad vendida 
    en cada combinación de sucursal y franja horaria.

    Returns:
        pd.DataFrame: DataFrame con columnas 
            ['sucursal', 'hora', 'minuto', 'producto', 'descuento', 'cantidad_vendida', 'total_ventas'],
            ordenado por sucursal, hora y minuto.
    """

    def __init__(self, db):
        self.db = db

    def analyze(self) -> pd.DataFrame:
        start = time.time()
        query = "SELECT * FROM vw_top_product_by_branch_hour_minute;"
        df = self.db.execute_query_as_dataframe(query)
        end = time.time()
        
        print(f"Tiempo de ejecución: {end - start:.3f} segundos")
        print("🔹 Ventas consolidadas por sucursal, hora/minuto y producto mas vendido")
        return df
