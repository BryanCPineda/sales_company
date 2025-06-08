# 🧾 Sistema de Análisis de Ventas

Este proyecto simula el flujo profesional de análisis de ventas de una compañía que opera en varias ciudades.  
El sistema está diseñado para trabajar con una base de datos relacional (MySQL) y una aplicación escrita en Python, modelada utilizando los principios de **Programación Orientada a Objetos (POO)** y buenas prácticas de desarrollo.

---

## 📁 Estructura de Carpetas

```
sales_company/
├── data/                           # Archivos CSV originales
├── notebooks/                      # Jupyter notebook para análisis
│   └── sales_analysis_demo.ipynb
├── sql/                            # Scripts para crear tablas, cargar datos, creacion de indices, procedimientos almacenados y vistas.
│   └── create_indexes.sql          # Agrega los índices recomendados para performance.
│   └── create_procedure.sql        # Crea los procedimientos almacenados utilizados en el sistema.
│   └── create_views.sql            # Crea las vistas necesarias para los informes.
│   └── load_data.sql               # Carga los datos iniciales desde los archivos CSV.
├── src/
│   └── core/                       # Configuracion de las variables de entorno y validaciones
│   └── database/                   # Configuracion de la conexion a la base de datos
│   └── models/                     # Clases que representan las entidades del negocio
│   └── services/                   # Servicio centralizado para ejecutar y coordinar reportes estratégicos de ventas.
│   └── strategies/                 # Estrategias para el analisis de ventas.
│   └── utils/                      # Funciones de utilidad, logger
├── test/                           # Pruebas unitarias con pytest
├── .env                            # Configuración de conexión a base de datos
├── .gitignore                      # Exclusiones de control de versiones
├── requirements.txt                # Dependencias del proyecto
├── README.md                       # Documentación del sistema
```

---

## 🛠 Requisitos Técnicos

- Python **3.12+**
- MySQL Server **8.0+**
- Paquetes de Python:
  - `pandas`
  - `sqlalchemy`
  - `python-dotenv`
  - `pytest`
  - _(otros que se encuentren en `requirements.txt`)_

---

## Cómo crear el entorno virtual e instalar dependencias

```bash
# Crear entorno virtual
python -m venv venv_sales_company

# Activar entorno virtual
# En Windows:
venv\Scripts\activate
# En GitBash desde windows:
source venv\Scripts\activate
# En Mac/Linux:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

---

## 🔐 Configuración del archivo `.env`

Crear un archivo `.env` en la raíz del proyecto con los siguientes valores:

```env
DB_HOST=localhost
DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña
DB_NAME=sales_company
DB_PORT=3306
```

---

## 🧩 Cómo cargar los datos en MySQL Workbench

1. Abrir MySQL Workbench e iniciar sesión.
2. Ejecutar el script SQL `sql/load_data.sql` que:

   - Crea la base de datos `sales_company`.
   - Crea todas las tablas necesarias.
   - Carga los archivos `.csv` desde la carpeta `/data/` usando `LOAD DATA LOCAL INFILE` ( ver script `sql/load_data.sql`).

     💡 Asegúrate de que la ruta a los archivos `.csv` sea absoluta y compatible con `LOAD DATA LOCAL INFILE` (por ejemplo, `C:/ruta/proyecto/data/archivo.csv`).

3. Asegurarse de tener habilitada la opción `local_infile` tanto en el servidor como en el cliente (ver errores `Error Code: 3948` o `2068` si no está habilitado).

---

# 🧱 Diseño del sistema

## 🔐 clases y modelos

Cada tabla del sistema tiene una clase Python correspondiente en la carpeta `models/`:

- `Category`, `City`, `Country`, `Customer`, `Employee`, `Product`, `Sale`

Cada clase:

- Usa **encapsulamiento** (`__atributo`)
- Tiene **constructores personalizados**
- Incluye **métodos útiles** para el negocio (como `get_full_name`, `get_tenure`, `apply_discount`, etc.)
- Implementa `__repr__` para facilitar debugging

---

## 🧱 Patrones de diseño implementados:

### Patron de diseño singleton

- Uso del patron de diseño Singleton en `database/connection.py` para generar una unica conexion a la base de datos, con el fin de centralizar la conexion y no generar nuevas conexiones innecesarias

### 📌 Consideraciones sobre la elección de patrones de diseño para análisis de ventas

Siguiendo la consigna propuesta en el inicio del proyecto

<img src="requerimientos.png" width="700">

Durante la etapa de diseño se evaluó la posibilidad de implementar el patrón Builder, con el objetivo de ofrecer a la dirección ejecutiva un conjunto de herramientas flexibles y personalizables para construir consultas ad hoc, agregando filtros, agrupaciones y condiciones según la necesidad puntual de cada análisis.

Sin embargo, el relevamiento de requerimientos dejó en claro que la necesidad principal de la dirección ejecutiva está enfocada en informes periódicos (diarios y mensuales) de estructura fija y lógica estable, orientados a:

- Informes periodicos diarios y mensuales ( en este caso, utilizando horas y minutos como equivalentes, ya que la informacion de fechas de ventas se encuentra en formato de tipo `TIME`)

- Consolidar ventas por sucursal (en este caso, utilizando ciudades como equivalentes de sucursales)

- Detectar patrones de comportamiento de los clientes

- Medir el rendimiento de productos y promociones

Dado que la cantidad de informes es acotada y sus criterios son bien definidos, se optó por el patrón Strategy para encapsular y desacoplar cada análisis relevante (por sucursal, por hora, por producto, etc.).

Esto permite:

- Profundizar en la calidad y el detalle de cada informe

- Asegurar una implementación ágil y mantenible

- Facilitar la extensión futura (agregando nuevas estrategias según la evolución del negocio)

En resumen:
Se priorizó una arquitectura menos flexible pero más reutilizable y robusta para los análisis requeridos, implementando diferentes estrategias de análisis de ventas que consoliden la información diaria y mensual ( horas y minutos ), detecten patrones de comportamiento y midan el rendimiento de productos y promociones.

### Patron de diseño Strategy:

- Uso del patron de diseño Strategy en `stragies/` para el analisis de ventas:
  - `sales_by_branch_and_hour`: Estrategia de análisis que identifica, para cada sucursal, hora y minuto,
    el producto más vendido y el descuento aplicado.
  - `sales_customer_behavior`: Estrategia de análisis de patrones de comportamiento de los clientes. Permite obtener
    - El total gastado, cantidad de transacciones y desglose de gasto con/sin promoción para cada cliente.
    - La sucursal donde el cliente gastó más (ciudad de mayor gasto).
    - El producto más comprado por cada cliente.
  - `sales_product_performance`: Estrategia de análisis de rendimiento de productos por sucursal. Permite identificar el top 5 productos más vendidos, con detalle de unidades vendidas, facturación total y ventas con/sin promoción.

### Patron de diseño Facade:

- Uso del patron de diseño facade en `services/report_service` para el acceso a las diferentes estrategias:
  - Servicio centralizado para ejecutar y coordinar reportes estratégicos de ventas.
  - Encapsula la lógica para ejecutar diferentes estrategias de análisis.
  - Permite a la capa de presentación acceder a los distintos análisis de negocio de forma simple y desacoplada.

## 🔍 Consultas SQL avanzadas y Objetos SQL

### Vistas

- Con el fin de lograr un mayor desacoplamiento, flexibilidad en el acceso y análisis de los datos, y permitir la reutilizacion y combinacion de resultados se decidio crear las siguientes vistas:

  - `sql/create_views.sql` -- vw_top_product_by_branch_hour_minute:

    - Uso de la funcion ventana `ROW_NUMBER()` para obtener la numeracion unica de manera secuencial
      - Descripción: Devuelve, para cada sucursal (ciudad), hora y minuto, el producto más vendido (mayor cantidad) y su descuento.
      - Uso: `SELECT \* FROM vw_top_product_by_branch_hour_minute;`

  - `sql/create_views.sql` -- vw_customer_behavior:
    - Uso de la funcion ventana `ROW_NUMBER()` para obtener la numeracion unica de manera secuencial
      - Descripción: Resumen ejecutivo del comportamiento de los clientes.
      - Uso: `SELECT * FROM vw_customer_behavior;`

### Procedimientos almacenados

- Se implementó un procedimiento almacenado (store procedure) `sql/create_procedures.sql` -- sp_top_products_by_branch:
  - Uso de la funcion ventana `DENSE_RANK()` para obtener valores de productos empatados con la numeracion continua sin saltos.
  - Con el fin de centralizar la lógica de obtención de los productos más vendidos por sucursal, optimizando la ejecución de consultas complejas, facilitando su mantenimiento.
    - Descripción: Devuelve, para cada sucursal (ciudad), el top N productos más vendidos, con detalle de unidades vendidas, facturación y ventas con/sin promoción.
    - Parámetros: `IN top_n INT` -- _Número de productos a retornar por sucursal (ranking)_
    - Uso: `CALL sp_top_products_by_branch(3);`

### Indices

- Se implementaron indices que buscaban optimizar las consultas:

  - Acelera JOINs y agrupamientos por cliente en ventas: `CREATE INDEX idx_sales_customerid ON sales(CustomerID);`

  - Acelera JOINs y agrupamientos por producto en ventas: `CREATE INDEX idx_sales_productid ON sales(ProductID);`

  - Acelera búsquedas y agrupaciones por fecha/hora de venta: `CREATE INDEX idx_sales_salesdate ON sales(SalesDate);`

_En este entorno y con la cantidad de datos actual, la creación de índices no tuvo impacto visible en los tiempos de ejecución del procedimiento almacenado. vease(`notebooks/sales_analysis_demo.ipynb -> Implementacion de indices`). Esto se debe a que el volumen de datos es moderado y la consulta realiza agregaciones sobre toda la tabla, donde el optimizador de MySQL prefiere un escaneo completo. En escenarios productivos con millones de registros y consultas filtradas, los índices aportan mejoras significativas en la performance._

## 📊 Notebook interactivo

En la carpeta `notebooks/` se incluye el archivo `sales_analysis_demo.ipynb`, que muestra:

- Conexión y consulta a la base de datos
- Ejemplo del patrón Singleton en acción
- Conversión de resultados a DataFrame con `pandas`
- Implementacion de los patrones `Strategy` y `Facade`
- Creacion de consultas avanzadas utilizando `CTE`, `Funciones de ventana` y `Objetos SQL`
- Implementacion de `Indices`
- Ejecución de pruebas con `pytest` desde el entorno de Jupyter

## 🧪 Cómo ejecutar los tests en Python

Los tests están ubicados en la carpeta `test/`.

Para correrlos usar el siguiente comando desde la raiz del proyecto:

```bash
pytest
```

Los tests unitarios validan:

- Que los métodos como `get_full_name` y `get_price` funcionen correctamente
- Que los setters actualicen atributos privados
- Que las representaciones (`__repr__`) devuelvan los valores esperados
- Que el patron singleton aplicado a la conexion con las base de datos funcione correctamente.

---

## 💡 Conclusiones y Justificación técnica

- Se utilizó **MySQL** como base de datos relacional, la cual brinda soporte de carga masiva de datos, y compatibilidad con herramientas del ecosistema.
- La carga de datos se realizó mediante `LOAD DATA LOCAL INFILE`, priorizando eficiencia en comparación con inserciones fila por fila.
- Las clases en Python están diseñadas bajo **principios de POO** para permitir la reutilización, validación de datos, y crecimiento futuro del sistema.
- El **patrón Singleton** aplicado a la conexión permite mantener una única instancia activa de conexión a la base de datos durante la ejecución del sistema.
- El **patrón Strategy** permite desacoplar y organizar múltiples algoritmos de análisis de ventas, haciendo el sistema flexible, escalable y fácilmente extensible ante nuevos requerimientos.
- El **patrón Facade** centraliza y simplifica el acceso a los diferentes informes analíticos, permitiendo a la capa de presentación interactuar con los análisis de negocio de forma sencilla y desacoplada.
- Las **vistas SQL** contribuyen a desacoplar y reutilizar la lógica de consulta, facilitando el análisis y reporte de información estratégica.
- El **procedimiento almacenado** centraliza y optimiza la obtención del ranking de productos más vendidos por sucursal, simplificando la lógica y mejorando la mantenibilidad.
- Aunque **los índices** no demostraron mejoras significativas de performance en este entorno de prueba, su incorporación deja al sistema preparado para escalar y soportar grandes volúmenes de datos en ambientes productivos.
- `pytest` fue elegido como framework de testing por su simplicidad, velocidad y facilidad de integración con proyectos en Python moderno.

---

⚠️ A tener en cuenta
Si bien la forma más adecuada de trabajar con SQLAlchemy es mediante el mapeo ORM de las clases y la carga de datos directamente a través del código Python, en este proyecto se optó por utilizar el script load_data.sql para la carga inicial.
Esta decisión se tomó por motivos prácticos y para cumplir con las consignas establecidas, priorizando agilidad en el desarrollo y pruebas.

## 🚀 Próximos pasos y mejoras

- **Integración completa del ORM**: Migrar gradualmente la lógica de consultas y manipulación de datos hacia SQLAlchemy en modo ORM, permitiendo aprovechar validaciones automáticas, relaciones entre entidades y mayor seguridad en las operaciones.

- **Automatización del pipeline de carga**: Implementar scripts o pipelines automatizados para la ingestión y validación de datos, facilitando actualizaciones periódicas y reducción de errores humanos.

- **Ampliación de informes y dashboards**: Incorporar nuevos análisis, reportes y visualizaciones (por ejemplo, integración con herramientas de BI como Power BI o Tableau).

- **Control de acceso y autenticación**: Añadir mecanismos de autenticación de usuarios y perfiles de acceso a los distintos informes y funcionalidades del sistema.

- **Optimización y monitoreo de performance**: Continuar evaluando el impacto de índices y planes de ejecución, e incorporar monitoreo automatizado para identificar cuellos de botella ante el crecimiento de datos.
