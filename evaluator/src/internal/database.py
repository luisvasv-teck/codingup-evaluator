import pandas as pd
import sqlite3
from src.common.database import Sqlite
from src.common.utilities import Application, Struct

class Actions:

    def __init__(self, app: Struct):
        self.__app = app
        
    def select_simple(self, query: str, parameters: tuple):
        connection: sqlite3.Connection = None
        sqlite = Sqlite(self.__app.app.profile.database)
        try:
            connection = sqlite.get_connection()
            sqlite.execute_single(query, parameters)
        except Exception as ex:
            print(f"an error occurred inserting the data:\n {ex}")
        finally:
            connection.close()
    
        def select_dataframe(self, query: str, parameters: tuple):
            connection: sqlite3.Connection = None
            sqlite = Sqlite(self.__app.profile.database)
            try:
                connection = sqlite.get_connection()
                sqlite.read_sql_query(query)
            except Exception as ex:
                print(f"an error occurred inserting the data:\n {ex}")
            finally:
                connection.close()
    
    
    
        def select_dataframe(self, sql: str):
        return pd.read_sql_query(sql, self.__conn)

    


    @property
    def get_cursor(self):
        return self.__cursor


    
    def select_dataframe(self, sql: str):
        return pd.read_sql_query(sql, self.__conn)
        
    def execute_single(self, sql: str, parameters: Tuple[Any, Any]):
        self.__cursor.execute(sql, parameters)
    
    def execute_many(self, sql: str, parameters: Tuple[Any, Any]):
        self.__cursor.executemany(sql, parameters)
