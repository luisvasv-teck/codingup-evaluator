class Messages:

    @staticmethod
    def get_language(list_values: list, profile_name: str) -> str:
        message_conf_file: str = (
                "\n[INFO]\n"
                f"\nthe profile '{profile_name}' already exists, do you want to replace it?\n\n"
                + '\n'.join(list_values)
                + "\n\nNote: input one of the values that are inside the ()\n" +
                "option: "
            )
        return message_conf_file

    @staticmethod
    def get_languages(list_values: list) -> str:
        message_language: str =  (
                    "\nplease: select the language with which you will teach the course, possible values:\n\n"
                    + '\n'.join(list_values) 
                    + "\n\nNote: input one of the values that are inside the ()\n" +
                    "option: "
                )
        return message_language

    @staticmethod
    def get_logotypes(list_values: list) -> str:
        message_logo: str =  (
                "\nplease: select a logotype to use in the header console, possible values:\n\n"
                + '\n'.join(list_values) 
                + "\n\nNote: intput one of the values that are inside the ()\n" +
                "option: "
            )
        return message_logo


class Generics:

    def print_header(message: str, size = 90, delimiter = "*") -> None:
        print('\n' + delimiter * size)
        print(message)
        print('\n' + delimiter * size)