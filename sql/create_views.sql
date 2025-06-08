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