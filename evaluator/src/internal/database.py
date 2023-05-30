import pandas as pd
import sqlite3
from typing import Tuple, Any
from src.common.database import Sqlite
from src.common.utilities import Application, Struct


class Actions(Sqlite):

    def __init__(self, app: Struct):
        self.__app = app
        super().__init__(self.__app.profile.database)
        
    def select_simple_2(self, query: str, parameters: tuple):
        connection: sqlite3.Connection = None
        try:
            connection = self.get_connection
            self.select_simple(query)
        except Exception as ex:
            print(f"an error occurred getting the data:\n {ex}")
        finally:
            connection.close()
    
    def select_query_dataframe(self, query: str) -> pd.DataFrame:
        connection: sqlite3.Connection = None
        df: pd.DataFrame = None
        try:
            connection = self.get_connection
            df = self.select_dataframe(query)
        except Exception as ex:
            print(f"an error occurred getting the data:\n {ex}")
        finally:
            connection.close()
        return df
       
    def execute_create_insert_update(self, sql: str, parameters: Tuple[Any, Any]):
        connection: sqlite3.Connection = None
        try:
            connection = self.get_connection
            if parameters is not None :
                self.execute_single(sql, parameters)
            else:
                self.select_simple(sql)
            connection.commit()
        except Exception as ex:
            print(f"an error has occurred with the DML/DDL:\n {ex}")
            exit(1)
        finally:
            connection.close()