import re

class Mail:
    __headers = {}
    __body = b""
    def __init__(self, mail_text):
        self.__headers, self.__body = mail_text.split(b"\r\n\r\n", 1)

    def get_body(self):
        return self.__body
    
    def get_headers(self):
        return self.__headers