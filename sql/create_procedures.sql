-- ============================================
-- Procedimiento almacenado: sp_top_products_by_branch
-- Descripción: Devuelve, para cada sucursal (ciudad), el top N productos más vendidos,
--              con detalle de unidades vendidas, facturación y ventas con/sin promoción.
-- Parámetros:
--   IN top_n INT   -- Número de productos a retornar por sucursal (ranking)
--
-- Uso:
--   CALL sp_top_products_by_branch(3);
--
-- ============================================
DELIMITER //
CREATE PROCEDURE sp_top_products_by_branch(IN top_n INT)
BEGIN
    WITH productos_por_sucursal AS (
        SELECT
            ct.CityName AS sucursal,
            p.ProductID,
            p.ProductName,
            SUM(s.Quantity) AS unidades_vendidas,
            SUM(s.TotalPrice) AS total_facturado,
            SUM(CASE WHEN s.Discount > 0 THEN s.Quantity ELSE 0 END) AS unidades_con_promocion,
            SUM(CASE WHEN s.Discount = 0 THEN s.Quantity ELSE 0 END) AS unidades_sin_promocion,
            RANK() OVER (PARTITION BY ct.CityName ORDER BY SUM(s.Quantity) DESC) AS ranking
        FROM sales s
        JOIN products p ON s.ProductID = p.ProductID
        JOIN customers c ON s.CustomerID = c.CustomerID
        JOIN cities ct ON c.CityID = ct.CityID
        GROUP BY ct.CityName, p.ProductID, p.ProductName
    )
    SELECT *
    FROM productos_por_sucursal
    WHERE ranking <= top_n;
END //
