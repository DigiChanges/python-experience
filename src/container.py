from injector import Binder, Module, singleton

from src.Shared.Helpers.Responder import Responder
from src.Auth.Services.AuthService import AuthService
from src.Role.Infrastructure.RoleRepository import RoleRepository
from src.User.Infrastructure.UserRepository import UserRepository

from src.Auth.InterfaceAdapters.IAuthService import IAuthService
from src.Role.InterfaceAdapters.IRoleRepository import IRoleRepository
from src.User.InterfaceAdapters.IUserRepository import IUserRepository


class Container(Module):

    def configure(self, binder: Binder) -> None:
        binder.bind(Responder, scope=singleton)
        binder.bind(IAuthService, AuthService)
        binder.bind(IRoleRepository, RoleRepository)
        binder.bind(IUserRepository, UserRepository)
