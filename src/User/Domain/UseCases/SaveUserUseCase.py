from src.User.InterfaceAdapters.IUserRepository import IUserRepository
from src.lazyInject import lazyInject

class SaveUserUseCase:

    repository: IUserRepository = lazyInject.get(IUserRepository)

    def handle(self, payload):
        print("Hi!")
        self.repository.save(payload)
        return payload
