from abc import ABC, abstractmethod


class ICriteriaPayload(ABC):

    @abstractmethod
    def getPagination(self) -> dict:
        pass

    @abstractmethod
    def getFilter(self) -> dict:
        pass

    @abstractmethod
    def getSort(self) -> dict:
        pass

    @abstractmethod
    def getCurrentUrl(self) -> str:
        pass