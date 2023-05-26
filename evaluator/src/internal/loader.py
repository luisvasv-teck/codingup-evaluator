import os
from __meta__ import  __root_config__, __app__
from src.common.utilities import Application, Struct
from src.common.constants import Constants
from src.common.database import Sqlite
from src.models.loader import Loader

class DataLoader:
    
    def __init__(self, args: dict):
        self.__args = args
    
    def __load_profile(self) -> Struct:
        profile_config: str = Application.read_yaml(
            os.path.join(
                __root_config__,
                "config",
                "profiles",
                f"{self.__args.profile_name}.yaml"
            )
        )
        profile = Struct(**profile_config)
        print(Application.get_header(Application.read_file(profile.logotype), __app__))
        return profile

    def __get_app_instances(self, profile: Struct) -> Loader:
        loader = Loader()
        loader.args = self.__args
        loader.constants = Constants()
        loader.profile = profile
        loader.utilities = Application
        loader.db = Sqlite(profile.database)
        return loader

            
            
    def start(self):
        # TODO agregar json schema para validar que no este corrupto
        app = self.__get_app_instances(self.__load_profile())
        
        # TODO: add db inicializaer
        # TODO: crear utilidad para ejecutar consultas
        return app


    # leer configuracion -- ok
    # cargar logo
    # iniciar ejecución programa
    # definir  seión de base de datos
    # devolver instancia de objetos