from abc import ABC, abstractmethod
from src.Role.Domain.Entities.Role import Role
from src.Shared.InterfaceAdapters.ICriteria import ICriteria


class IRoleRepository(ABC):

    @abstractmethod
    def save(self, element) -> Role:
        pass

    @abstractmethod
    def getOne(self, id: str) -> Role:
        pass

    @abstractmethod
    def list(self, criteria: ICriteria):
        pass

    @abstractmethod
    def delete(self, id: str):
        pass
