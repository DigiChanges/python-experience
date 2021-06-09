from abc import ABC, abstractmethod
from typing import List


class RoleUpdateRepPayload(ABC):
    name: str
    slug: str
    enable: bool
    permissions: List[str]

    @abstractmethod
    def getName(self):
        pass

    @abstractmethod
    def getSlug(self):
        pass

    @abstractmethod
    def getEnable(self):
        pass

    @abstractmethod
    def getPermissions(self):
        pass
