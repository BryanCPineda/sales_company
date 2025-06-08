from abc import ABC, abstractmethod
from typing import List
import pandas as pd

class SalesAnalysisStrategy(ABC):
    @abstractmethod
    def analyze(self) -> pd.DataFrame:
        """
        Ejecuta el análisis de ventas y devuelve un DataFrame con los resultados.

        :return: pandas.DataFrame con los datos procesados del análisis
        """
        pass