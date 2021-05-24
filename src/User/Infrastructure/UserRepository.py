from injector import inject
from dataclasses import dataclass

from src.User.Domain.Entities.User import User
from src.User.Infrastructure.UserDocument import UserDocument
from src.User.InterfaceAdapters.IUserRepository import IUserRepository


@inject
@dataclass
class UserRepository(IUserRepository):
    def save(self, payload: User):
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

        print("Save User", user)
