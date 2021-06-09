from abc import ABC, abstractmethod
from typing import Any, List

class IAuthService(ABC):

    @abstractmethod
    def decodeToken(self, token: str) -> Any:
        pass

    @abstractmethod
    def getPermissions(self, user: Any) -> List[str]:
        pass
    # def getPermissions(user: IUserDomain) -> List[str]:

    @abstractmethod
    def validatePermissions(self, permissions: List[str]) -> None:
        pass