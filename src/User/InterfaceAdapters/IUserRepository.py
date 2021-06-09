from abc import ABC, abstractmethod
from src.Shared.InterfaceAdapters.ICriteria import ICriteria
from src.Shared.InterfaceAdapters.IPaginator import IPaginator


class IUserRepository(ABC):

    @abstractmethod
    def save(self, element):
        pass

    @abstractmethod
    def getOne(self, id: str):
        pass

    @abstractmethod
    def list(self, criteria: ICriteria) -> IPaginator:
        pass

    @abstractmethod
    def delete(self, id: str):
        pass

    @abstractmethod
    def getOneByEmail(self, email: str):
        pass

    @abstractmethod
    def getOneByConfirmationToken(self, confirmationToken: str):
        pass

