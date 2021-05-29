from src.User.InterfaceAdapters.IUserRepository import IUserRepository
from src.User.InterfaceAdapters.Payloads.UserUpdateRepPayload import UserUpdateRepPayload
from src.lazyInject import lazyInject


class UpdateUserUseCase:

    repository: IUserRepository = lazyInject.get(IUserRepository)

    def handle(self, payload: UserUpdateRepPayload, id):

        user = self.repository.getOne(id)

        user.firstName = payload.getFirstName()
        user.lastName = payload.getLastName()
        user.email = payload.getEmail()
        user.birthday = payload.getBirthday()
        user.documentType = payload.getDocumentType()
        user.documentNumber = payload.getDocumentNumber()
        user.gender = payload.getGender()
        user.phone = payload.getPhone()
        user.country = payload.getCountry()
        user.address = payload.getAddress()
        user.enable = payload.getEnable()
        user.permissions = payload.getPermissions()

        return self.repository.save(user)
