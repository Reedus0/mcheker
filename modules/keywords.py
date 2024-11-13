import re
import requests

from modules.module import Module
from config import *

class Keywords(Module):
    __keywords = [
        "gov", "docx", "pdf", "xlsx", "document", "attachment",
        "password", "encrypted", "protected"
    ]

    def check_keywords(self, mail_body):
        results = []

        for keyword in self.__keywords:
            if (keyword in mail_body):
                results.append(keyword)

        return { "spam": True if len(results) > KEYWORDS_LIMIT else False, "check": "keywords check", "detail": results }


    def check_mail(self, mail):
        results = []
        results.append(self.check_keywords(mail.get_body().decode()))

        self._output = { "module": "keywords", "detail": results }