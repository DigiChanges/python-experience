from fastapi import Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from src.Auth.Domain.Exceptions.InvalidTokenException import InvalidTokenException
from src.Auth.Domain.Exceptions.TokenNotFoundException import TokenNotFoundException
from src.Auth.InterfaceAdapters.IAuthService import IAuthService
from src.lazyInject import lazyInject


class JWTBearer(HTTPBearer):

    authService: IAuthService = lazyInject.get(IAuthService)

    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise InvalidTokenException() # Invalid authentication scheme.
            if not self.verify_jwt(credentials.credentials):
                raise InvalidTokenException()
            return credentials.credentials
        else:
            raise TokenNotFoundException()
            # raise HTTPException(status_code=403, detail="Invalid authorization code.")

    def verify_jwt(self, jwtoken: str) -> bool:
        isTokenValid: bool = False

        try:
            payload = self.authService.decodeToken(jwtoken)
        except:
            payload = None

        if payload:
            isTokenValid = True

        return isTokenValid