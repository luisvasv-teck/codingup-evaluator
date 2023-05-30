import os
from src.common.utilities import Application
from __meta__ import  __root_config__

class GetList:
    
    def get_languages():
        defaut_config = Application.read_yaml(os.path.join(__root_config__, "config", "default", "app.yaml"))
        options: dict = dict([(value["id"],key) for key, value in defaut_config["languages"].items()])
        options_text: list = [f"({key}) - {value}" for key, value in options.items()]
        return options, options_text, True 
    
    def get_logotypes():
        with_data: bool = False
        logotypes_folder: str = os.path.join(__root_config__, 'logotypes')
        if not Application.is_empty_folder(logotypes_folder):
            with_data = True
            logotypes: dict = dict([(key + 1, value) for key, value in enumerate(os.listdir(logotypes_folder))])
            logotypes_text = [f"({index}) - {value}" for index, value in logotypes.items()]
        return logotypes, logotypes_text, with_data
    
    def get_yes_no():
        conditions: dict = dict([(key + 1, value) for key, value in enumerate(["yes", "no"])])
        conditions_text: list = [f"({key}) - {value}" for key, value in conditions.items()]
        return conditions, conditions_text, True 