from abc import ABC, abstractmethod


class IUserRepository(ABC):

    @abstractmethod
    def save(self, user):
        pass