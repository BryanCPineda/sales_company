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
        query = """
        WITH
          -- Gasto por cliente y sucursal
          gasto_por_sucursal AS (
              SELECT 
                  c.CustomerID,
                  ct.CityName AS sucursal,
                  SUM(s.TotalPrice) AS total_gastado_sucursal,
                  ROW_NUMBER() OVER (PARTITION BY c.CustomerID ORDER BY SUM(s.TotalPrice) DESC) AS rn_sucursal
              FROM customers c
              JOIN sales s ON c.CustomerID = s.CustomerID
              JOIN cities ct ON c.CityID = ct.CityID
              GROUP BY c.CustomerID, ct.CityName
          ),

          -- Cantidad comprada por cliente y producto
          productos_cliente AS (
              SELECT 
                  c.CustomerID,
                  p.ProductName,
                  SUM(s.Quantity) AS cantidad_comprada,
                  ROW_NUMBER() OVER (PARTITION BY c.CustomerID ORDER BY SUM(s.Quantity) DESC) AS rn_producto
              FROM customers c
              JOIN sales s ON c.CustomerID = s.CustomerID
              JOIN products p ON s.ProductID = p.ProductID
              GROUP BY c.CustomerID, p.ProductName
          ),

          -- Resumen general por cliente
          resumen_cliente AS (
              SELECT 
                  c.CustomerID,
                  CONCAT(c.FirstName, ' ', c.LastName) AS cliente,
                  SUM(s.TotalPrice) AS total_gastado,
                  COUNT(s.SalesID) AS transacciones,
                  SUM(CASE WHEN s.Discount > 0 THEN s.TotalPrice ELSE 0 END) AS gastado_con_promocion,
                  SUM(CASE WHEN s.Discount = 0 THEN s.TotalPrice ELSE 0 END) AS gastado_sin_promocion
              FROM customers c
              JOIN sales s ON c.CustomerID = s.CustomerID
              GROUP BY c.CustomerID, cliente
          )

          SELECT 
              rc.CustomerID,
              rc.cliente,
              rc.total_gastado,
              rc.transacciones,
              rc.gastado_con_promocion,
              rc.gastado_sin_promocion,
              gps.sucursal AS sucursal_donde_mas_gasto,
              pc.ProductName AS producto_mas_comprado
          FROM resumen_cliente rc
          LEFT JOIN gasto_por_sucursal gps
              ON rc.CustomerID = gps.CustomerID AND gps.rn_sucursal = 1
          LEFT JOIN productos_cliente pc
              ON rc.CustomerID = pc.CustomerID AND pc.rn_producto = 1
          ORDER BY rc.total_gastado DESC
          LIMIT 20;
        """
        
        start = time.time()
        df = self.db.execute_query_as_dataframe(query)
        end = time.time()
        
        print(f"Tiempo de ejecución: {end - start:.3f} segundos")
        print("🔹 Top clientes por gasto y aprovechamiento de promociones:")
        return df