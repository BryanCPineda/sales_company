-- ================================================
-- Índices recomendados para optimizacion en las consultas
-- ================================================

-- Acelera JOINs y agrupamientos por cliente en ventas
CREATE INDEX idx_sales_customerid ON sales(CustomerID);

-- Acelera JOINs y agrupamientos por producto en ventas
CREATE INDEX idx_sales_productid ON sales(ProductID);

-- Acelera búsquedas y agrupaciones por fecha/hora de venta
CREATE INDEX idx_sales_salesdate ON sales(SalesDate);