-- ============================================
-- Vista: vw_top_product_by_branch_hour_minute
-- Descripción: Devuelve, para cada sucursal (ciudad), hora y minuto,
--              el producto más vendido (mayor cantidad) y su descuento.
-- Uso:
--    SELECT * FROM vw_top_product_by_branch_hour_minute;
--
-- ============================================

CREATE OR REPLACE VIEW vw_top_product_by_branch_hour_minute AS
WITH ventas_agrupadas AS (
    SELECT 
        ct.CityName AS sucursal,
        HOUR(s.SalesDate) AS hora,
        MINUTE(s.SalesDate) AS minuto,
        p.ProductName AS producto,
        s.Discount AS descuento,
        SUM(s.Quantity) AS cantidad_vendida,
        SUM(s.TotalPrice) AS total_ventas
    FROM sales s
    JOIN customers c ON s.CustomerID = c.CustomerID
    JOIN cities ct ON c.CityID = ct.CityID
    JOIN products p ON s.ProductID = p.ProductID
    GROUP BY sucursal, hora, minuto, producto, descuento
)
SELECT 
    sucursal,
    hora,
    minuto,
    producto,
    descuento,
    cantidad_vendida,
    total_ventas
FROM (
    SELECT 
        *,
        ROW_NUMBER() OVER (PARTITION BY sucursal, hora, minuto ORDER BY cantidad_vendida DESC) AS rn
    FROM ventas_agrupadas
) ranked
WHERE rn = 1
ORDER BY sucursal, hora, minuto;

-- ===============================================================
-- Vista: vw_customer_behavior
-- Descripción:
--     Resumen ejecutivo del comportamiento de los clientes.
--     Para los 20 clientes con mayor gasto total, muestra:
--         - Nombre y monto total gastado
--         - Número de transacciones realizadas
--         - Total gastado con y sin promoción
--         - Sucursal donde más gastó (por monto)
--         - Producto más comprado (por cantidad)
--
--     Utiliza CTEs y funciones ventana (ROW_NUMBER) para calcular
--     sucursal y producto más relevantes por cliente.
--
-- Uso:
--     SELECT * FROM vw_customer_behavior;
-- ============================================

CREATE OR REPLACE VIEW vw_customer_behavior AS
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