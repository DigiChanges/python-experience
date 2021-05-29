from injector import inject
from dataclasses import dataclass

from src.Shared.InterfaceAdapters.ICriteria import ICriteria
from src.User.Domain.Entities.User import User
from src.User.InterfaceAdapters.IUserRepository import IUserRepository


@inject
@dataclass
class UserRepository(IUserRepository):
    def save(self, element):
        return element.save()

    def getOne(self, id: str):
        return User.objects.get(id=id)

    def list(self, criteria: ICriteria):
        data = User.objects()
        return data

    def delete(self, id: str):
        return User.objects.get(id=id)

    def getOneByEmail(self, email: str):
        return User.objects.get(email=email)

    def getOneByConfirmationToken(self, confirmationToken: str):
        return User.objects.get(confirmationToken=confirmationToken)
