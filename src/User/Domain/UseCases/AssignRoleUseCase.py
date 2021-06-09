
from src.lazyInject import lazyInject
from src.Role.InterfaceAdapters.IRoleRepository import IRoleRepository
from src.User.Domain.Entities.User import User
from src.User.InterfaceAdapters.IUserRepository import IUserRepository
from src.User.InterfaceAdapters.Payloads.UserAssignRolePayload import UserAssignRolePayload


class AssignRoleUseCase:

    repository: IUserRepository = lazyInject.get(IUserRepository)

    roleRepository: IRoleRepository = lazyInject.get(IRoleRepository)

    def handle(self, payload: UserAssignRolePayload, id: str):

        user: User = self.repository.getOne(id)

        user.clearRoles()

        for roleId in payload.getRolesId():
            role = self.roleRepository.getOne(roleId)
            user.setRole(role)

        self.repository.save(user)

        return self.repository.save(user)
