
class NotAllowed(Exception):
    def __init__(self, message: str):
        super().__init__()
        self.__message = message

    def message(self) -> str:
        return self.__message
