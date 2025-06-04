from src.database.connection import DatabaseConnection
from sqlalchemy import text
import pandas as pd

def main():
    try:
        db = DatabaseConnection()
        #session = db.get_session()
        
        # result = session.execute(text("SELECT COUNT(*) FROM customers"))
        # count = result.scalar()
        # print(f"Número de clientes en la base de datos: {count}")

        # result = session.execute(text("SELECT * FROM categories"))
        # rows = result.fetchall()
        # print(f"Categorias:")
        # for row in rows:
        #     print(f"- ID: {row[0]}, Nombre: {row[1]}")

        # result = session.execute(text("SELECT * FROM categories"))
        # df = pd.DataFrame(result.fetchall(), columns=result.keys())
        # print(df)

        # db.close_session(session)

        query = "SELECT * FROM employees"
        df = db.execute_query_as_dataframe(query)
        print("Resultados de la consulta:")
        print(df)

    except Exception as e:
        print("Error al conectar a la base de datos:", e)

if __name__ == "__main__":
    main()