from src.strategies.sales_analysis_strategy import SalesAnalysisStrategy
import pandas as pd
import time

class ProductPerformanceStrategy(SalesAnalysisStrategy):
    """
    Estrategia de análisis de rendimiento de productos por sucursal.

    Utiliza CTE y función ventana RANK para obtener, por cada sucursal (ciudad), 
    el top 5 productos más vendidos, con detalle de unidades vendidas, 
    facturación total y ventas con/sin promoción.

    Returns:
        pd.DataFrame: DataFrame con las columnas
            ['sucursal', 'ProductID', 'ProductName', 'unidades_vendidas', 
            'total_facturado', 'unidades_con_promocion', 
            'unidades_sin_promocion', 'ranking'],
            ordenado por sucursal y ranking.
    """
    def __init__(self, db, top_n=5):
        """
        Args:
            db: Objeto de conexión a la base de datos.
            top_n (int): Cantidad de productos top a mostrar por sucursal.
        """
        self.db = db
        self.top_n = top_n

    def analyze(self) -> pd.DataFrame:
        start = time.time()
        query = f"CALL sp_top_products_by_branch({self.top_n});"
        df = self.db.execute_query_as_dataframe(query)
        end = time.time()
        
        print(f"Tiempo de ejecución: {end - start:.3f} segundos")
        print(f"🔹 Top {self.top_n} productos más vendidos por sucursal:")
        return df