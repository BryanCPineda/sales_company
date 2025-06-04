from src.database.connection import DatabaseConnection
from sqlalchemy.engine import Connection
from sqlalchemy.orm import Session
import pandas as pd

def test_singleton_instance():
    """Verifica que DatabaseConnection implemente correctamente el patrón Singleton."""
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()

    assert db1 is db2, "DatabaseConnection no está funcionando como Singleton"

def test_get_session():
    """Verifica que get_session retorne una instancia de Session."""
    db = DatabaseConnection()
    session = db.get_session()
    assert isinstance(session, Session)
    db.close_session(session)

def test_close_session():
    """Verifica que close_session no lance error al cerrar una sesión."""
    db = DatabaseConnection()
    session = db.get_session()
    try:
        db.close_session(session)
        closed = True
    except Exception:
        closed = False
    assert closed, "close_session falló al cerrar la sesión"

def test_execute_query_as_dataframe():
    """Verifica que una consulta simple se ejecute y devuelva un DataFrame válido."""
    db = DatabaseConnection()
    df = db.execute_query_as_dataframe("SELECT * FROM categories")
    assert isinstance(df, pd.DataFrame), "El resultado no es un DataFrame"
    assert df.columns is not None, "El DataFrame no tiene columnas"