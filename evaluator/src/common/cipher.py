from cryptography.fernet import Fernet


class AES:

    def __init__(self, key: bytes = None):
        if key is None:
            self.__key = self.__generate_key()
        else:
            self.__key = key.encode('utf-8')

    def __generate_key(self):
        key = Fernet.generate_key() 
        return key

    def get_key(self) -> str:
        return self.__key.decode('utf-8')

    def encrypt_value(self, value: str):
        fernet = Fernet(self.__key)
        encrypted_value = fernet.encrypt(value.encode('utf-8'))
        return encrypted_value

    def decrypt_value(self, encrypted_value: str):
        fernet = Fernet(self.__key)
        decrypted_value = fernet.decrypt(encrypted_value).decode('utf-8')
        return decrypted_value
