from abc import ABC, abstractmethod


class AuthPayload(ABC):

    @abstractmethod
    def getEmail(self) -> str:
        raise Exception("Not implemented")

    @abstractmethod
    def getPassword(self) -> str:
        raise Exception("Not implemented")