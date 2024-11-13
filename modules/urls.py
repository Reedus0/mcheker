import re
import requests

from modules.module import Module

class Urls(Module):

    __hosts = []

    def query_urlhaus(self, host):
        data = {
            "host": host
        }

        response = requests.post("https://urlhaus-api.abuse.ch/v1/host/", data)
        json_response = response.json()
        if json_response["query_status"] == "ok":
            return json_response
        elif json_response["query_status"] == "no_results":
            return "No results"
        else:
            return json_response["query_status"]

    def check_urlhaus(self):
        results = []

        for host in self.__hosts:
            host_test_result = self.query_urlhaus(host.decode())
            if (host_test_result != "No results"):
                results.append(host_test_result)

        return { "spam": True if len(results) else False, "check": "urlhaus check", "detail": results }
    
    def check_subdomains(self):
        results = []

        for host in self.__hosts:
            subdomains = host.split(b".")[:-1]
            for subdomain in subdomains:
                if (len(subdomain.decode()) > 8):
                    results.append(host.decode())

        return { "spam": True if len(results) else False, "check": "subdomains check", "detail": results }


    def check_mail(self, mail):
        results = []
        self.__hosts = set(re.findall(rb"https?:\/\/([\w\d.]+)", mail.get_body()))

        results.append(self.check_urlhaus())
        results.append(self.check_subdomains())

        self._output = { "module": "urls", "detail": results }