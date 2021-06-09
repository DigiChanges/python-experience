from src.Role.Domain.Entities.Role import Role
from src.Role.InterfaceAdapters.IRoleRepository import IRoleRepository
from src.Role.InterfaceAdapters.Payloads.RoleRepPayload import RoleRepPayload
from src.lazyInject import lazyInject


class SaveRoleUseCase:

    repository: IRoleRepository = lazyInject.get(IRoleRepository)

    def handle(self, payload: RoleRepPayload):

        role = Role()
        role.name = payload.getName()
        role.slug = payload.getSlug()
        role.enable = payload.getEnable()
        role.permissions = payload.getPermissions()

        return self.repository.save(role)
