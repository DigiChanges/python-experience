from abc import ABC, abstractmethod
from typing import Any, List

class IAuthService(ABC):

    @abstractmethod
    def decodeToken(token: str) -> Any:
        pass

    @abstractmethod
    def getPermissions(user: Any) -> List[str]:
        pass
    # def getPermissions(user: IUserDomain) -> List[str]:

    @abstractmethod
    def validatePermissions(permissions: List[str]) -> None:
        pass