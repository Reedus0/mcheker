import re

class Mail:
    __headers = {}
    __body = b""
    def __init__(self, mail_body):
        self.__headers, self.__body = mail_body.split(b"\r\n\r\n", 1)

    def get_body(self):
        return self.__body
    
    def get_headers(self):
        return self.__headers