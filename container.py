from injector import Binder, Module, singleton

from src.Shared.Responder import Responder
from src.User.Infrastructure.UserRepository import UserRepository
from src.User.InterfaceAdapters.IUserRepository import IUserRepository


class Container(Module):

    def configure(self, binder: Binder) -> None:
        binder.bind(Responder, scope=singleton)
        binder.bind(IUserRepository, UserRepository)
