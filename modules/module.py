class Module:
    _results = []
    _output = { "module": "default", "detail": "Module class" }

    def check_mail(self, mail):
        pass

    def get_output(self):
        if ("module" not in self._output or "detail" not in self._output):
            return {"module": "default", "detail": "Failed to validate module results" }
        return self._output