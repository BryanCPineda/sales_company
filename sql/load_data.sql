-- Crear base de datos sales_company (si no existe)
DROP DATABASE IF EXISTS sales_company;
CREATE DATABASE IF NOT EXISTS sales_company; 
USE sales_company;

-- Crear tabla categories (si no existe)
DROP TABLE IF EXISTS categories;
CREATE TABLE categories (
    CategoryID INT PRIMARY KEY,
    CategoryName VARCHAR(45)
);

-- Crear tabla cities (si no existe)
DROP TABLE IF EXISTS cities;
CREATE TABLE cities (
    CityID INT PRIMARY KEY,
    CityName VARCHAR(45),
    Zipcode VARCHAR(10),
    CountryID INT
);


-- Crear tabla countries (si no existe)
DROP TABLE IF EXISTS countries;
CREATE TABLE countries (
    CountryID INT PRIMARY KEY,
    CountryName VARCHAR(100),
    CountryCode VARCHAR(10)
);

-- Crear tabla customers (si no existe)
DROP TABLE IF EXISTS customers;
CREATE TABLE customers (
    CustomerID INT PRIMARY KEY,
    FirstName VARCHAR(100),
    MiddleInitial CHAR(5),
    LastName VARCHAR(100),
    CityID INT,
    Address VARCHAR(255)
);


-- Crear tabla employees (si no existe)
DROP TABLE IF EXISTS employees;
CREATE TABLE employees (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(100),
    MiddleInitial CHAR(1),
    LastName VARCHAR(100),
    BirthDate DATETIME,
    Gender CHAR(1),
    CityID INT,
    HireDate DATETIME
);

-- Crear tabla products (si no existe)
DROP TABLE IF EXISTS products;
CREATE TABLE products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(255),
    Price DECIMAL(10, 4),
    CategoryID INT,
    Class VARCHAR(50),
    ModifyDate TIME,
    Resistant VARCHAR(50),
    IsAllergic VARCHAR(10),
    VitalityDays INT
);

-- Crear tabla sales (si no existe)
DROP TABLE IF EXISTS sales;
CREATE TABLE sales (
    SalesID INT PRIMARY KEY,
    SalesPersonID INT,
    CustomerID INT,
    ProductID INT,
    Quantity INT,
    Discount DECIMAL(4, 2),
    TotalPrice DECIMAL(10, 2),
    SalesDate TIME,
    TransactionNumber VARCHAR(50)
);

-- Asegurarse de que local infile esta habilitado para cargar datos desde archivos locales
SET GLOBAL local_infile = 1;
SHOW GLOBAL VARIABLES LIKE 'local_infile';


-- Cargar datos desde los archivo CSV
    -- Asegurarse de que el archivo CSV existe en la ruta especificada
    -- Modificar las rutas de los archivos CSV según sea necesario
-- Cargar datos de categories
LOAD DATA LOCAL INFILE 'C:/Users/bcami/OneDrive/Escritorio/ACCENTURE/sales_company/data/categories.csv'
INTO TABLE categories
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- Cargar datos de cities
LOAD DATA LOCAL INFILE 'C:/Users/bcami/OneDrive/Escritorio/ACCENTURE/sales_company/data/cities.csv'
INTO TABLE cities
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- Cargar datos de countries
LOAD DATA LOCAL INFILE 'C:/Users/bcami/OneDrive/Escritorio/ACCENTURE/sales_company/data/countries.csv'
INTO TABLE countries
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- Cargar datos de customers
LOAD DATA LOCAL INFILE 'C:/Users/bcami/OneDrive/Escritorio/ACCENTURE/sales_company/data/customers.csv'
INTO TABLE customers
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- Cargar datos de employees
LOAD DATA LOCAL INFILE 'C:/Users/bcami/OneDrive/Escritorio/ACCENTURE/sales_company/data/employees.csv'
INTO TABLE employees
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- Cargar datos de products
LOAD DATA LOCAL INFILE 'C:/Users/bcami/OneDrive/Escritorio/ACCENTURE/sales_company/data/products.csv'
INTO TABLE products
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- Cargar datos de sales
LOAD DATA LOCAL INFILE 'C:/Users/bcami/OneDrive/Escritorio/ACCENTURE/sales_company/data/sales.csv'
INTO TABLE sales
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

