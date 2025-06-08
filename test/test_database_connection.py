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
    
def test_execute_query_as_dataframe_invalid_query():
    """Verifica que una consulta inválida retorne un DataFrame vacío y loggee error."""
    db = DatabaseConnection()
    df = db.execute_query_as_dataframe("SELECT * FROM tabla_inexistente")
    assert isinstance(df, pd.DataFrame)
    assert df.empty
    
def test_excute_query_runs_without_error(monkeypatch):
    """Verifica que excute_query ejecute una consulta válida sin lanzar excepción."""
    db = DatabaseConnection()
    db.excute_query("CREATE OR REPLACE VIEW test_view AS SELECT 1 AS val;")
    db.excute_query("DROP VIEW IF EXISTS test_view;")

def test_excute_query_invalid_query():
    """Verifica que una consulta inválida en excute_query no lance excepción."""
    db = DatabaseConnection()
    try:
        db.excute_query("SELECT * FROM tabla_inexistente")
        ran = True
    except Exception:
        ran = False
    assert ran, "excute_query lanzó excepción ante un error de SQL"
    
def test_get_session_handles_exception(monkeypatch):
    """Simula un error al obtener sesión y verifica que se maneje correctamente."""
    db = DatabaseConnection()
    original_session = db.Session

    def raise_exception():
        raise Exception("Error de prueba")

    db.Session = raise_exception
    session = db.get_session()
    assert session is None
    db.Session = original_session  
    
def test_close_session_handles_exception(monkeypatch):
    """Simula un error al cerrar sesión y verifica que se maneje correctamente."""
    db = DatabaseConnection()
    class FakeSession:
        def close(self):
            raise Exception("Error de prueba")
    fake_session = FakeSession()
    db.close_session(fake_session)
    
    