from src.User.InterfaceAdapters.IUserRepository import IUserRepository
from src.lazyInject import lazyInject


class ListUserUseCase:
    repository: IUserRepository = lazyInject.get(IUserRepository)

    def handle(self):
        return self.repository.list(None)
