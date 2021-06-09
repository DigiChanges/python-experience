from abc import ABC, abstractmethod
from typing import List, Any


class IFilter(ABC):

    @abstractmethod
    def values(self) -> List: # Map<string, any>:
        pass

    @abstractmethod
    def get(self, key: str) -> Any:
        pass

    @abstractmethod
    def has(self, key: str) -> bool:
        pass

    @abstractmethod
    def isEmpty(self) -> bool:
        pass

    @abstractmethod
    def getFields(self) -> List:
        pass

    @abstractmethod
    def getDefaultFilters(self) -> Any:
        pass
