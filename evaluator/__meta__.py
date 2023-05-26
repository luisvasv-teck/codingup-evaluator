import os

__app__: str= "codingup-evaluator"
__basedir__: str = os.path.dirname(os.path.abspath(__file__))
__database_name__: str = "evaluator.db"
__header__: str = "SOFTSERVE"
__root_config__: str = os.path.join(__basedir__,  "resources")
__root_database__: str = os.path.join(__basedir__, "resources", "database")
