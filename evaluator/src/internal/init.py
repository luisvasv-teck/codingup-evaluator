import os
import yaml
from __meta__ import  __root_config__, __root_database__
from src.common.utilities import Application, Struct
from src.internal.lists import GetList
from src.internal.texts import Messages, Generics
from src.internal.database import Actions
from src.models.loader import Loader
from src.common.cipher import AES

class SetUpValidator:
    
    def __init__(self, args: dict):
        self.__args = args
        self.__app = Application.read_yaml(os.path.join(__root_config__, "config", "default", "app.yaml"))
        self.__cryp = AES()
    

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
        
        # get email info
        info["hash"] =  self.__cryp.get_key() 
       
        info["email"] = {
            "imap_server": Application.get_text_simple("input imamp server (smtp.demo.com): ", "imap_server"),
            "imap_port": Application.get_number_simple("input imamp port                  : ", "imap_port"),
            "smtp_server": Application.get_text_simple("input smtp server (smtp.demo.com) : ", "smtp_server"),
            "smtp_port": Application.get_number_simple("input smtp port                   : ", "port_port"),
            "account": Application.get_email("input email address               : ", "email"),
            "password": self.__cryp.encrypt_value(
                Application.get_password("input email password              : ", "password")
            ).decode('utf-8')
        }

        # create profile file
        with open(config_file, 'w') as file:
            documents = yaml.dump(info, file)
        print("")
        print("[STAGE 1/3] creating profile .............. [OK]")
        print("[STAGE 2/3] creating database ............. [OK]")
        print("[STAGE 3/2] creating table teachers........ [OK]")
        return info
    
    def __create_database(self, profile: dict):
        sql_teachers:str = Application.read_file(os.path.join(__root_config__, self.__app["init"]["db"]["teachers"]))
        loader = Loader()
        loader.args = self.__args
        loader.profile = Struct(**profile)
        
        actions = Actions(loader)
        actions.execute_create_insert_update(sql_teachers, ())
        print("[STAGE 3/2] creating table teachers........ [OK]")
        
    def validate_email(self, profile):
        pass
        
    def run(self):
        # TODO: replace process, delete db file
        # TODO: agregar validacion para carpetas de estilos html emails
        # getting config
        profile: dict = self.__config()
        
        # checking email
        
        # create file
        
        # create database
        self.__create_database(profile)
        
        # create database
        print(self.__args)
        
        
    
    