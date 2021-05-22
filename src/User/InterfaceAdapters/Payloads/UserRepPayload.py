from abc import ABC, abstractmethod

class UserRepPayload(ABC):

    @abstractmethod
    def getFirstName(self) -> str:
        pass

    @abstractmethod
    def getFirstName(self) -> str:
        pass

    @abstractmethod
    def getLastName(self) -> str:
        pass

    @abstractmethod
    def getEmail(self) -> str:
        pass

    @abstractmethod
    def getPassword(self) -> str:
        pass