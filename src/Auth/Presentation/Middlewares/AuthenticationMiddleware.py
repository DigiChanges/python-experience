from typing import Any, List

from src.Shared.Exceptions.DecryptForbiddenException import \
    DecryptForbiddenException
from starlette.authentication import (AuthCredentials, AuthenticationBackend,
                                      AuthenticationError, SimpleUser,
                                      UnauthenticatedUser)
from starlette.types import ASGIApp, Receive, Scope, Send


class AuthenticationMiddleware(AuthenticationBackend):
    witheList = [{"method": "POST", "url": "/api/auth/login"}]

    def __init__(self, app: ASGIApp) -> None:
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send):
        # raise AuthenticationError('Invalid basic auth credentials')
        # raise DecryptForbiddenException()
        await self.app(scope, receive, send)
        client = scope["client"]
        print(self.witheList)
        print(f"[CLIENT]: {client}")
