import logging
import getpass
import yaml
import os
import json
import re
from yaml.loader import SafeLoader
from datetime import datetime


class Application:

    """
    A class that allows managing the constant variables for system level
    """

    def __init__(self):
        self.__LOGGER: logging = None

    def set_logger(
        self,
        app_name: str,
        logger_level: int = logging.DEBUG
    ):
        """
            custom logger to use in the app
            :param app_name     : name of the application or floe that is running
            :param logger_level : logger level - CRITICAL=50, ERROR=40, WARNING=30,
                INFO=20, DEBUG=10, NOTSET=0
        """

        logger = logging.getLogger(app_name)
        logger.setLevel(logger_level)
        consoleHandler = logging.StreamHandler()
        consoleHandler.setLevel(logger_level)
        formatter = logging.Formatter(
            "[%(asctime)s] - [%(levelname)s] - [%(name)s] : %(message)s", "%d/%m/%Y %H:%M:%S"
        )
        consoleHandler.setFormatter(formatter)
        logger.addHandler(consoleHandler)
        self.__LOGGER = logger

    @property
    def LOGGER(self) -> logging.Logger:
        """
            allows to use a logger instance configured to store and print in console
        """
        return self.__LOGGER

    @staticmethod
    def read_yaml(path: str) -> dict:
        """allows to read a yaml file and return the contect as dict

        Args:
            path (str): yaml local path

        Returns:
            dict: Dictionary with the YAML context, otherwise return None
        """
        content: dict = None
        try:
            with open(path) as file:
                content = yaml.load(file, Loader=SafeLoader)
        except Exception:
            content = None
        return content

    @staticmethod
    def get_header(header: str, app: str, delimeter: str ="-" * 50) -> str:
        """
            It allows defining the header of the routine base, which will
            be shown every
            time the routine is executed

            parameters :
                header    :
                app       : aplication name
                delimeter : log separator delimiter

            outputs :
                header : text with the azlo logo execution date, app name
                        and with delimiter
        """
        format_date = "%Y/%m/%d/ %H:%M:%S"
        return header.format(delimeter, str(datetime.now().strftime(format_date)), app)

    @staticmethod
    def is_empty_null(value) -> bool:
        """
           allows validate if a string is empty

            parameters :
                value = string to evaluate

            outputs :
                list with specific values
        """
        state = False
        if value == "" or value is None:
            state = True
        return state

    @staticmethod
    def get_readable_json(dictionary: dict) -> str:
        """
            allows generate a dic vale in a json readable
            mode
            parameters :
                dictionary = dictionary object
            outputs :
               string in json format
        """
        info = json.dumps(dictionary, default=str)
        parsed = json.loads(info)
        return json.dumps(parsed, indent=4, sort_keys=True)

    @staticmethod
    def is_empty_folder(folder: str) -> bool:
        """check if the folder contain files

        Args:
            folder (str): _description_

        Returns:
            bool: true if it's empty, false otherwise
        """
        status = False
        try:

            if not os.path.isdir(folder):
                status = True
            else:
                files = [arch.name for arch in os.scandir(folder) if arch.is_file()]
                if len(files) == 0:
                    status = True
        except Exception:
            status = True
        return status

    @staticmethod
    def is_valid_file(file: str) -> bool:
        """check if the path corresponds to a file

        Args:
            file (str): path to validate

        Returns:
            bool: true if it's a file, false otherwise
        """
        status = True
        try:
            if not os.path.isfile(file):
                status = False
        except Exception:
            status = False
        return status

    @staticmethod
    def get_config_path() -> str:
        """
        allows obtaining the path of the configuration where the library was installed
        :return str config path
        """
        path: str = f"{os.sep}".join(os.path.abspath(__file__).split(os.sep)[:-1])
        return os.path.join(path, "config")

    @staticmethod
    def read_json(config_path: str, error_message: str) -> dict:
        """_summary_

        Args:
            config_path   (str): json path
            error_message (str): alternative error message

        Raises:
            Exception: if the json file doesn't exists

        Returns:
            dict: json content
        """
        data = {}
        try:
            with open(config_path) as config:
                data = json.load(config)
        except Exception as ex:
            raise Exception(error_message + str(ex))
        return data
    
    @staticmethod
    def print_config(data: dict, logger: logging.Logger) -> None:
        for key, value in data.items():
            if isinstance(value, dict):
                logger.info("variables['{}'] = {}".format(key, json.dumps(value, indent=4)))
            else:
                logger.info(f"variables['{key}'] = {value}")
                
    @staticmethod
    def get_text(text: str, possible_values, data_type):

        value=None
        while True:
            try:
                value = data_type(input(text))
                if value in possible_values:
                    break
            except Exception as ex:
                print(f"invalid value: {value}, try again.")
        return value
    
    @staticmethod
    def get_text_simple(text: str, key: str):
        value=None
        while True:
            try:
                value = input(text)
                if len(value.strip()):
                    break
            except Exception as ex:
                print(f"intunt a {key}, try again.")
        return value
    
    @staticmethod
    def get_email(text: str, key: str):
        pattern: str = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        email: str = None
        while True:
            try:
                email = input(text)
                if re.match(pattern, email):
                    break
            except Exception as ex:
                print(f"intunt a valid {key}, try again.")
        return email
    
    @staticmethod
    def get_number_simple(text: str, key: str, data_type = int):
        value=None
        while True:
            try:
                value = data_type(input(text))
                break
            except Exception as ex:
                print(f"intunt a {key}, try again.")
        return value
    
    @staticmethod
    def get_password(text: str, key: str, two_validations: bool = True):
        password_1: str = None
        while True:
            try:
                password_1 = getpass.getpass(text)
                if len(password_1.strip()) > 0:
                    if two_validations:
                        password_2 = Application.get_password(
                            text.replace("input", "repeat").replace("password ", "password"),
                            "repeat-{key}", False
                        )
                        if password_1 == password_2:
                            break
                    else:
                        break
            except Exception as ex:
                print(f"intunt a {key}, try again.")
        return password_1

    @staticmethod
    def read_file(file_path: str) -> str:
        with open(file_path, 'r') as file:
            content = file.read()
            return content

class Struct:
    """
    It allows through its constructor to send a dictionary and
    return an object structured with dictionary attributes.
    """

    def __init__(self, **config: dict):
        """
        class constructor Struct

        parameters :
            config : dictionary with the values
        outputs :
            struct objet

        usage:

            >>> from common.utilities import Struct
            >>> structure = Struct(**{'version':'1.0','createdby':'teck'})
            >>> structure.version
            1.0
            >>> structure.createdby
            teckW
        """
        self.__dict__.update(config)