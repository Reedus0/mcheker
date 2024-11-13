import os
import re
import requests

from modules.module import Module

class Blacklists(Module):
    __servers = []

    def check_mxtoolbox(self):
        results = []
        headers = {
            "Authorization": os.getenv("MXTOOLBOX_API_KEY")
        }

        for server in self.__servers:
            
            response = requests.get(f"https://mxtoolbox.com/api/v1/lookup/blacklist/{server.decode()}", headers=headers)
            json_response = response.json()
            blacklists = json_response["Failed"]

            for blacklist in blacklists:
                blacklist["Server"] = server.decode()
                results.append(blacklist)

        return { "spam": True if len(results) else False, "check": "keywords check", "detail": results }


    def check_mail(self, mail):
        results = []
        self.__servers = set(re.findall(rb"Received:\sfrom\s([\w\d.-]+)\s", mail.get_headers()))

        results.append(self.check_mxtoolbox())

        self._output = { "module": "blacklists", "detail": results }