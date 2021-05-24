from src.User.Infrastructure.UserDocument import UserDocument
from src.User.InterfaceAdapters.IUserRepository import IUserRepository
from src.User.InterfaceAdapters.Payloads.UserRepPayload import UserRepPayload
from src.lazyInject import lazyInject

class SaveUserUseCase:

    repository: IUserRepository = lazyInject.get(IUserRepository)

    def handle(self, payload: UserRepPayload):
        user = UserDocument()
        user.firstName = payload.firstName
        user.lastName = payload.lastName
        user.email = payload.email
        user.password = payload.password
        user.birthday = payload.birthday
        user.documentType = payload.documentType
        user.documentNumber = payload.documentNumber
        user.gender = payload.gender
        user.phone = payload.phone
        user.country = payload.country
        user.address = payload.address
        user.enable = payload.enable
        user.permissions = payload.permissions
        user.save()
        # self.repository.save(payload)

        return user
