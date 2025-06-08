from src.database.connection import DatabaseConnection
from sqlalchemy import text
import pandas as pd
from src.services.report_service import ReportService


def main():
    try:
        db = DatabaseConnection()
        
        report = ReportService(db)
        report.sales_by_branch_and_hour()
        report.customer_behavior()
        report.product_performance(3)
                
    except Exception as e:
        print("Error al conectar a la base de datos:", e)

if __name__ == "__main__":
    main()
