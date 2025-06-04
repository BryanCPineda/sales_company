import os
from dotenv import load_dotenv

load_dotenv()

"""
  Módulo de configuración para la conexión a la base de datos MySQL. 
  Carga las variables de entorno desde un archivo .env y construye la URL de conexión.
  Asegura que las variables críticas estén presentes y lanza un error si faltan.
"""

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", "3306"))
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

if not all([DB_USER, DB_PASSWORD, DB_NAME]):
    raise ValueError("Faltan variables críticas en el archivo .env")

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"