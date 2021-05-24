from injector import inject
from dataclasses import dataclass

from src.User.Domain.Entities.User import User
from src.User.InterfaceAdapters.IUserRepository import IUserRepository


@inject
@dataclass
class UserRepository(IUserRepository):
    def save(self, user: User):
        print("Save User")