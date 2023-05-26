import sqlite3
import pandas as pd
from typing import Tuple, Any, Dict


class Sqlite:
    
    def __init__(self, database: str):
        print(database)
        self.__conn = sqlite3.connect(database)
        self.__cursor = self.__conn.cursor()
        self.__cursor.execute("PRAGMA foreign_keys = ON")
        
    @property
    def get_connection(self):
        return self.__conn

    @property
    def get_cursor(self):
        return self.__cursor

    def select_simple(self, sql: str):
        self.__cursor.execute(sql)
        return self.__cursor.fetchall()
    
    def select_dataframe(self, sql: str):
        return pd.read_sql_query(sql, self.__conn)
        
    def execute_single(self, sql: str, parameters: Tuple[Any, Any]):
        self.__cursor.execute(sql, parameters)
    
    def execute_many(self, sql: str, parameters: Tuple[Any, Any]):
        self.__cursor.executemany(sql, parameters)
