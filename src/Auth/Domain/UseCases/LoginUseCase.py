from src.Auth.Shared.JWTToken import JWTToken
from src.Auth.AuthHandler import signJWT
from src.Shared.Exceptions.DecryptForbiddenException import DecryptForbiddenException
from src.Auth.InterfaceAdapters.Payloads.AuthPayload import AuthPayload
from src.lazyInject import lazyInject
from src.User.Infrastructure.UserDocument import UserDocument
from src.User.InterfaceAdapters.IUserRepository import IUserRepository
from src.User.InterfaceAdapters.Payloads.UserRepPayload import UserRepPayload
from src.Shared.Config import config


class LoginUseCase:

    repository: IUserRepository = lazyInject.get(IUserRepository)

    def handle(self, payload: AuthPayload):
        email = payload.getEmail()
        password = payload.getPassword()
        # self.repository.getOneByEmail(email)

        foundUser = UserDocument()
        foundUser.id = 12
        foundUser.email = email
        foundUser.firstName = "john"
        foundUser.lastName = "Doe"
        foundUser.enable = True


        if not foundUser.enable:
            raise DecryptForbiddenException()

        # compare encrypt pass
        # create token
        # token = signJWT(foundUser.email)

        expires = config["jwt"]["expires"]

        token = JWTToken( expires , foundUser)

        return token
