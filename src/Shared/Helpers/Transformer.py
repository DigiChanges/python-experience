import abc
from abc import abstractmethod
from typing import Any
from mongoengine import QuerySet

class Transformer(abc.ABC):

    @abstractmethod
    def transform(self, data: Any) -> Any:
        pass

    def handle(self, data: Any) -> Any:
        result = None

        if isinstance(data, QuerySet):
            result = list(map(lambda element: self.transform(element), data))
        else:
            result = self.transform(data)

        return result
