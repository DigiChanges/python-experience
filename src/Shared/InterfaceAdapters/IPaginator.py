from abc import ABC, abstractmethod
from typing import Any


class IPaginator(ABC):

    @abstractmethod
    def paginate(self) -> Any:
        pass

    @abstractmethod
    def getTotal(self) -> int:
        pass

    @abstractmethod
    def getCurrentUrl(self) -> str:
        pass

    @abstractmethod
    def getNextUrl(self) -> str:
        pass

    @abstractmethod
    def getExist(self) -> bool:
        pass