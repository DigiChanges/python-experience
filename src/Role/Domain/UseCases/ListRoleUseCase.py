from src.Role.InterfaceAdapters.IRoleRepository import IRoleRepository
from src.lazyInject import lazyInject


class ListRoleUseCase:
    repository: IRoleRepository = lazyInject.get(IRoleRepository)

    def handle(self):
        return self.repository.list(None)
