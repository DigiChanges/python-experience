from src.Shared.InterfaceAdapters.ICriteria import ICriteria
from src.Shared.InterfaceAdapters.IPaginator import IPaginator
from src.User.InterfaceAdapters.IUserRepository import IUserRepository
from src.lazyInject import lazyInject


class ListUserUseCase:
    repository: IUserRepository = lazyInject.get(IUserRepository)

    def handle(self, payload: ICriteria) -> IPaginator:
        return self.repository.list(payload)
