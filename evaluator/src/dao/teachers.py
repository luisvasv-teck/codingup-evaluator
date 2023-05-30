import pandas as pd
from tabulate import tabulate
from src.internal.database import Actions
from src.common.utilities import Application, Struct

class Teachers(Actions):
    # mostrar datos
    # insertar usuario
    # actualizar estado
    def __init__(self, app: Struct):
        self.__app = app
        super().__init__(self.__app)
    
    def select_teachers(self) -> pd.DataFrame:
        params : dict = {"active": self.__app.args.active}
        select: str = self.__app.config.sql["teachers"]["select"]
        print("\n")
        print(tabulate(self.select_query_dataframe(select.format(**params)), headers='keys', tablefmt='psql', showindex=False))
        print("\n")
    
    def inactivate_teacher(self):
        id: str = self.__app.args.id
        active: str = 'N'
        params : dict = {"id": id, "active": active}
        print("\n")
        insert: str = self.__app.config.sql["teachers"]["update"]
        self.execute_create_insert_update(insert.format(**params), None)
        print(f"teacher {id} upated successfully.")
        
    def add_teacher(self):
        print("\n")
        id: str = Application.get_text_simple("intput teacher id        : ","teacher-id")
        name: str = Application.get_text_simple("intput teacher full name : ","full-name")
        email: str = Application.get_email("intput teacher email     : ","email")
        active: str = 'Y'
        print("\n")
        insert: str = self.__app.config.sql["teachers"]["insert"]
        self.execute_create_insert_update(insert, (id, name, email, active))
        print(f"teacher {id} inserted successfully.")
            
            
# TODO: agregar validacion para exportar datos al formato definido
    