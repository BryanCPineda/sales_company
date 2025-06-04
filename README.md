# 🧾 Sistema de Análisis de Ventas

Este proyecto simula el flujo profesional de análisis de ventas de una compañía que opera en varias ciudades.  
El sistema está diseñado para trabajar con una base de datos relacional (MySQL) y una aplicación escrita en Python, modelada utilizando los principios de **Programación Orientada a Objetos (POO)** y buenas prácticas de desarrollo.

---

## 📁 Estructura de Carpetas

```
sales_company/
├── data/               # Archivos CSV originales
├── sql/                # Scripts para crear tablas y cargar datos
├── src/
│   └── models/         # Clases que representan las entidades del negocio
├── test/               # Pruebas unitarias con pytest
├── .env                # Configuración de conexión a base de datos
├── .gitignore          # Exclusiones de control de versiones
├── requirements.txt    # Dependencias del proyecto
├── README.md           # Documentación del sistema
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
python -m venv venv

# Activar entorno virtual
# En Windows:
venv\Scripts\activate
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
   - Carga los archivos `.csv` desde la carpeta `/data/` usando `LOAD DATA LOCAL INFILE`.
3. Asegurarse de tener habilitada la opción `local_infile` tanto en el servidor como en el cliente (ver errores `Error Code: 3948` o `2068` si no está habilitado).

---

## 🧱 Diseño del sistema: clases y modelos

Cada tabla del sistema tiene una clase Python correspondiente en la carpeta `models/`:

- `Category`, `City`, `Country`, `Customer`, `Employee`, `Product`, `Sale`

Cada clase:

- Usa **encapsulamiento** (`__atributo`)
- Tiene **constructores personalizados**
- Incluye **métodos útiles** para el negocio (como `get_full_name`, `get_tenure`, `apply_discount`, etc.)
- Implementa `__repr__` para facilitar debugging

---

## 🧪 Cómo ejecutar los tests

Los tests están ubicados en la carpeta `test/`.

Para correrlos usar el comando:

Desde la raiz del proyecto

```bash
pytest
```

Los tests unitarios validan:

- Que los métodos como `get_full_name` y `get_price` funcionen correctamente
- Que los setters actualicen atributos privados
- Que las representaciones (`__repr__`) devuelvan los valores esperados

---

## 💡 Justificación técnica

- Se utilizó **MySQL** como base de datos relacional, la cual brinda soporte de carga masiva de datos, y compatibilidad con herramientas del ecosistema.
- La carga de datos se realizó mediante `LOAD DATA LOCAL INFILE`, priorizando eficiencia en comparación con inserciones fila por fila.
- Las clases en Python están diseñadas bajo **principios de POO** para permitir la reutilización, validación de datos, y crecimiento futuro del sistema.
- `pytest` fue elegido como framework de testing por su simplicidad, velocidad y facilidad de integración con proyectos en Python moderno.

---
