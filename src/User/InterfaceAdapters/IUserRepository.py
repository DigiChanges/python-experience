from abc import ABC, abstractmethod
from src.User.Domain.Entities.User import User


class IUserRepository(ABC):

    @abstractmethod
    def save(self, user: User):
        pass