from src.Shared.Factories.EncryptionFactory import EncryptionFactory
from src.Shared.InterfaceAdapters.IEncryption import IEncryption
from src.User.Domain.Entities.User import User
from src.User.InterfaceAdapters.IUserRepository import IUserRepository
from src.User.InterfaceAdapters.Payloads.UserRepPayload import UserRepPayload
from src.lazyInject import lazyInject


class SaveUserUseCase:

    repository: IUserRepository = lazyInject.get(IUserRepository)
    encryption: IEncryption = EncryptionFactory.create()

    def handle(self, payload: UserRepPayload):
        if payload.passwordValidation():
            raise Exception("Error password validation")

        user = User()
        user.firstName = payload.getFirstName()
        user.lastName = payload.getLastName()
        user.email = payload.getEmail()
        user.password = self.encryption.encrypt(payload.getPassword())
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
