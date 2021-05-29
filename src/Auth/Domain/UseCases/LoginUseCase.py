from src.Shared.Factories.EncryptionFactory import EncryptionFactory
from src.Shared.InterfaceAdapters.IEncryption import IEncryption
from src.User.Domain.Entities.User import User
from src.Auth.Domain.Exceptions.BadCredentialsException import BadCredentialsException
from src.Auth.InterfaceAdapters.Payloads.AuthPayload import AuthPayload
from src.Auth.Shared.JWTToken import JWTToken
from src.lazyInject import lazyInject
from src.Shared.Config import config
from src.User.Domain.Exceptions.UserDisabledException import UserDisabledException
from src.User.InterfaceAdapters.IUserRepository import IUserRepository
from datetime import datetime, timedelta


class LoginUseCase:

    repository: IUserRepository = lazyInject.get(IUserRepository)
    encryption: IEncryption = EncryptionFactory.create()

    def handle(self, payload: AuthPayload):
        email = payload.getEmail()
        password = payload.getPassword()

        user: User = self.repository.getOneByEmail(email)

        if not user.enable:
            raise UserDisabledException()

        if not self.encryption.compare(password, user.password):
            raise BadCredentialsException()

        jwtExpires = config.get("jwt", {}).get("expires")

        expire = datetime.utcnow() + timedelta(minutes=jwtExpires)

        token = JWTToken( expire , user)

        return token
