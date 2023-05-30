class Constants:

    """
    Class that allows to manage the constant variables of the program,
    is carried out as a class and using the hint @properties to ensure
    that the value is not modified during the time
    of execution
    """

    def __init__(self):
        self.__OK: int = 0
        self.__ERROR: int = -1

    @property
    def OK(self):
        """
            It allows to indicate that the process was carried out correctly
            without errors.
        """
        return self.__OK

    @property
    def ERROR(self):
        """
            It indicates that there were internal coding errors, normally
            captured by means of an exception.
        """
        return self.__ERROR
