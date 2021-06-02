from fastapi import Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from src.Auth.Domain.Exceptions.ForbiddenException import ForbiddenException
from src.Auth.Domain.Exceptions.InvalidTokenException import InvalidTokenException
from src.Auth.Domain.Exceptions.TokenNotFoundException import TokenNotFoundException
from src.Auth.InterfaceAdapters.IAuthService import IAuthService
from src.lazyInject import lazyInject
from src.User.Domain.Entities.User import User
from src.User.Infrastructure.UserRepository import UserRepository
from src.User.InterfaceAdapters.IUserRepository import IUserRepository


class JWTBearer(HTTPBearer):

    authService: IAuthService = lazyInject.get(IAuthService)
    userRepository: UserRepository = lazyInject.get(IUserRepository)

    tokenPayload = None
    handlerPermission: str = None

    def __init__(self, permission = None, auto_error: bool = True):
        self.handlerPermission = permission
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise InvalidTokenException() # Invalid authentication scheme.
            if not self.verify_jwt(credentials.credentials):
                raise InvalidTokenException()

            isAllowed: bool = False

            user: User = self.userRepository.getOneByEmail(self.tokenPayload.get("email"))
            if user.isSuperAdmin:
                isAllowed = True

            totalPermissions = self.authService.getPermissions(user)

            for permission in totalPermissions:
                if permission == self.handlerPermission:
                    isAllowed = True

            if not isAllowed:
                raise ForbiddenException()

            return credentials.credentials
        else:
            raise TokenNotFoundException()
            # raise HTTPException(status_code=403, detail="Invalid authorization code.")

    def verify_jwt(self, jwtoken: str) -> bool:
        isTokenValid: bool = False

        try:
            self.tokenPayload = self.authService.decodeToken(jwtoken)
        except:
            self.tokenPayload = None

        if self.tokenPayload:
            isTokenValid = True

        return isTokenValid