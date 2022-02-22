from typing import Callable


class BasePoint:
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def discover() -> list:
        result = []
        return result

    @staticmethod
    def get(_address: str, _object: str, _object_instance: str) -> object:
        result = []
        return result

    def write(self, value):
        return self

    def cov(
            self,
            _address: str,
            _object: str,
            _object_instance: str,
            _callback: Callable[[str, str, str], object],
            _confirmed: bool = True,
            _lifetime=None,
    ):
        return self
