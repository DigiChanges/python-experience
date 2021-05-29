
from abc import ABC, abstractmethod
from typing import Any, Dict

from src.User.Domain.Entities.User import User

class IToken(ABC):

    @abstractmethod
    def getExpires(self) -> int:
        pass

    @abstractmethod
    def getHash(self) -> str:
        pass

    @abstractmethod
    def getPayload(self) -> Dict[str, str]:
        pass

    @abstractmethod
    def getUser(self) -> User:
        pass