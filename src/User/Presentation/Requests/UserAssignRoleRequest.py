from pydantic import BaseModel
from src.User.InterfaceAdapters.Payloads.UserAssignRolePayload import UserAssignRolePayload
from typing import List


class UserAssignRoleRequest(UserAssignRolePayload, BaseModel):
    rolesId: List[str] = []

    def getRolesId(self):
        return self.rolesId
