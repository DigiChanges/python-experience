from abc import ABC, abstractmethod
from src.User.Domain.Entities.User import User


class IUserDomain(ABC):

    @abstractmethod
    def save(self, user: User):
        pass