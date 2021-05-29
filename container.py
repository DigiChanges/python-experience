from injector import Binder, Module, singleton

from src.Shared.Helpers.Responder import Responder
from src.User.Infrastructure.UserRepository import UserRepository
from src.Auth.Services.AuthService import AuthService

from src.Auth.InterfaceAdapters.IAuthService import IAuthService
from src.User.InterfaceAdapters.IUserRepository import IUserRepository


class Container(Module):

    def configure(self, binder: Binder) -> None:
        binder.bind(Responder, scope=singleton)
        binder.bind(IAuthService, AuthService)
        binder.bind(IUserRepository, UserRepository)
