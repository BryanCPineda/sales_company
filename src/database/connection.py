import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, scoped_session
from src.core.config import DATABASE_URL
from src.utils.logger import get_logger
import pandas as pd

logger = get_logger(__name__)

class DatabaseConnection:
    """
    Clase de tipo Singleton responsable de manejar la conexión a la base de datos MySQL utilizando SQLAlchemy.

    Esta clase garantiza que sólo exista una única instancia de conexión activa durante el ciclo de vida
    de la aplicación. Permite obtener sesiones, ejecutar consultas y cerrar conexiones de forma segura.
    """
    _instance = None

    def __new__(cls):
        """
        Crea una instancia única de DatabaseConnection si no existe.

        Returns:
            DatabaseConnection: Instancia única de la clase.
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            try:
                cls._instance.engine = create_engine(DATABASE_URL, echo=False)
                cls._instance.Session = scoped_session(
                    sessionmaker(bind=cls._instance.engine)
                )
            except Exception as e:
                raise RuntimeError(f"Error al conectar a la base de datos: {e}")
        return cls._instance

    def get_session(self):
        """
        Obtiene una nueva sesión de base de datos.

        Returns:
            Session: Sesión SQLAlchemy activa o None si hubo un error.
        """
        try:
            logger.info("Obteniendo sesión de la base de datos...")
            return self.Session()
        except Exception as e:
            logger.error(f"Error al obtener la sesión: {e}")
            return None

    def close_session(self, session):
        """
        Cierra una sesión de base de datos previamente abierta.

        Args:
            session (Session): Sesión SQLAlchemy a cerrar.
        """
        try:
            logger.info("Cerrando sesión de la base de datos...")
            session.close()
        except Exception as e:
            logger.error(f"Error al cerrar la sesión: {e}")

    def execute_query_as_dataframe(self, query: str, params: dict = None) -> pd.DataFrame:
        """
        Ejecuta una consulta SQL y devuelve los resultados en formato DataFrame.

        Args:
            query (str): Consulta SQL a ejecutar.
            params (dict, optional): Parámetros para consultas parametrizadas.

        Returns:
            pandas.DataFrame: Resultados de la consulta como DataFrame. Vacío si hay error.
        """
        try:
            logger.info(f"Ejecutando consulta: {query}")
            with self.engine.connect() as connection:
                result = connection.execute(text(query), params or {})
                df = pd.DataFrame(result.fetchall(), columns=result.keys())
                return df
        except Exception as e:
            logger.error(f"Error al ejecutar la consulta: {str(e)}")
            return pd.DataFrame()



