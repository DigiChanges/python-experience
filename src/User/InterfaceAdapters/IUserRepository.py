from abc import ABC, abstractmethod
from src.User.Domain.Entities.User import User
from src.Shared.InterfaceAdapters.ICriteria import ICriteria


class IUserRepository(ABC):

    @abstractmethod
    def save(self, element):
        pass

    @abstractmethod
    def getOne(self, id: str):
        pass

    @abstractmethod
    def list(self, criteria: ICriteria):
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

