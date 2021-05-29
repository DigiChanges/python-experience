from src.User.InterfaceAdapters.IUserRepository import IUserRepository
from src.lazyInject import lazyInject


class GetOneUserUseCase:
    repository: IUserRepository = lazyInject.get(IUserRepository)

    def handle(self, id: str):
        return self.repository.getOne(id)
