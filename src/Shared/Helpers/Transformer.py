import abc
from abc import abstractmethod
from typing import Any, List


class Transformer(abc.ABC):

    @abstractmethod
    def transform(self, data: Any) -> Any:
        pass

    def handle(self, data: Any) -> Any:
        result = None

        if isinstance(data, List):
            pass
            # result = data.map((element: any) =>
            # {
            #     return this.transform(element);
            # });
        else:
            result = self.transform(data)

        return result
