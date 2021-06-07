from src.Role.InterfaceAdapters.IRoleRepository import IRoleRepository
from src.lazyInject import lazyInject


class GetOneRoleUseCase:
    repository: IRoleRepository = lazyInject.get(IRoleRepository)

    def handle(self, id: str):
        return self.repository.getOne(id)
