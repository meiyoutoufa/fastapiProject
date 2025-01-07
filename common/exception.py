
class MyException(Exception):
    def __init__(self, detail: str, code: int = 500):
        self.detail = detail
        self.code = code