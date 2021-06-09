from abc import ABC, abstractmethod
from typing import List


class ISort(ABC):

    @abstractmethod
    def get(delf) -> dict:
        pass

    @abstractmethod
    def getFields(self) -> List[str]:
        pass

    @abstractmethod
    def getDefaultSorts(self) -> dict:
        pass