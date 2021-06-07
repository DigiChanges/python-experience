from typing import List
from pydantic import BaseModel
from src.Role.InterfaceAdapters.Payloads.RoleUpdateRepPayload import RoleUpdateRepPayload


class RoleUpdateRepRequest(RoleUpdateRepPayload, BaseModel):
    name: str
    slug: str
    enable: bool
    permissions: List[str] = []

    def getName(self):
        return self.name

    def getSlug(self):
        return self.slug

    def getEnable(self):
        return self.enable

    def getPermissions(self):
        return self.permissions
