from src.Role.InterfaceAdapters.IRoleRepository import IRoleRepository
from src.Role.InterfaceAdapters.Payloads.RoleUpdateRepPayload import RoleUpdateRepPayload
from src.lazyInject import lazyInject


class UpdateRoleUseCase:

    repository: IRoleRepository = lazyInject.get(IRoleRepository)

    def handle(self, payload: RoleUpdateRepPayload, id):

        role = self.repository.getOne(id)

        role.name = payload.getName()
        role.slug = payload.getSlug()
        role.enable = payload.getEnable()
        role.permissions = payload.getPermissions()

        return self.repository.save(role)
