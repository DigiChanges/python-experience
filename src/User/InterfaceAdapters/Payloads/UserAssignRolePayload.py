from abc import ABC, abstractmethod


class UserAssignRolePayload(ABC):

    @abstractmethod
    def getRolesId(self):
        pass
