from abc import ABC, abstractmethod

from src.Shared.InterfaceAdapters.IFilter import IFilter
from src.Shared.InterfaceAdapters.IPagination import IPagination
from src.Shared.InterfaceAdapters.ISort import ISort


class ICriteria(ABC):

    @abstractmethod
    def getPagination(self) -> IPagination:
        pass

    @abstractmethod
    def getFilter(self) -> IFilter:
        pass

    @abstractmethod
    def getSort(self) -> ISort:
        pass
