from injector import inject
from dataclasses import dataclass

from src.Shared.InterfaceAdapters.ICriteria import ICriteria
from src.Role.Domain.Entities.Role import Role
from src.Role.InterfaceAdapters.IRoleRepository import IRoleRepository


@inject
@dataclass
class RoleRepository(IRoleRepository):
    def save(self, element) -> Role:
        return element.save()

    def getOne(self, id: str) -> Role:
        print('id')
        print(id)
        role = Role.objects.get(id=id)
        print('role')
        print(role)

        return role

    def list(self, criteria: ICriteria):
        data = Role.objects()
        return data

    def delete(self, id: str) -> Role:
        return Role.objects.get(id=id)
