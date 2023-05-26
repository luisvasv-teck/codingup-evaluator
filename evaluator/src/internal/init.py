import os
import yaml
from __meta__ import  __root_config__, __root_database__
from src.common.utilities import Application
from src.internal.lists import GetList
from src.internal.texts import Messages, Generics


class SetUpValidator:
    
    def __init__(self, args: dict):
        self.__args = args
    
    def __create_database(self):
        
        
        pass
    
    def __config(self):
        # config file
        config_file: str = os.path.join(__root_config__, "config", "profiles", f"{self.__args.profile_name}.yaml")
        if Application.is_valid_file(config_file):
            conditionals, conditionals_text, options_data = GetList.get_yes_no()
            Messages.get_language(conditionals_text, self.__args.profile_name)
            message_conf_file: str =  Messages.get_language(conditionals_text, self.__args.profile_name)
            answer: str = conditionals[Application.get_text(message_conf_file, conditionals, int)]
            if answer == "no":
                print("process canceled by user")
                exit(0)
                
        # set header
        Generics.print_header("generating new config")

        # set db path
        info: dict = {"database": os.path.join(__root_database__, f"{self.__args.profile_name}.db")}
        # set language
        languages, languages_text, options_data = GetList.get_languages()
        message_language: str =  Messages.get_languages(languages_text)
        info.update({"language": languages[Application.get_text(message_language, languages, int)]})

        # set logotype
        logotypes, logotypes_text, options_data = GetList.get_logotypes()
        if options_data:
            logotypes_folder: str = os.path.join(__root_config__, 'logotypes')
            message_logo: str = Messages.get_logotypes(logotypes_text)
            info.update(
                {
                    "logotype": os.path.join(logotypes_folder, logotypes[Application.get_text(message_logo, logotypes, int)])
                }
            )
        else:
            info.update({"logotype": "no_defined"})

        # create profile file
        with open(config_file, 'w') as file:
            documents = yaml.dump(info, file)

        print("[STAGE 1/3] profile has been created.")
        return info
        
    
    def __create_database(self):
        pass
    
    def run(self):
        # create config
        profile: dict = self.__config()
        
        # create database
        print(self.__args)
        
        
    
    