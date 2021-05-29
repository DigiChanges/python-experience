
from typing import Any

from fastapi import Request
from fastapi.responses import JSONResponse

from starlette.authentication import (AuthCredentials, AuthenticationBackend,
                                      AuthenticationError, SimpleUser,
                                      UnauthenticatedUser)


class ErrorHttpException:

    def __init__(self, app: Any):
        @app.exception_handler(FileNotFoundError)
        async def http_file_http_exception_handler(request: Request, exc: FileNotFoundError):
            return JSONResponse(
                status_code=500,
                content={"message": "Filesystem error."},
            )

        @app.exception_handler(AuthenticationError)
        async def http_authentication_exception_handler(request: Request, exc: AuthenticationError):
            return JSONResponse(
                status_code=403,
                content={"message": "Auth error."},
            )

        @app.exception_handler(Exception)
        async def http_general_http_exception_handler(request: Request, exc: Exception):
            return JSONResponse(
                status_code=500,
                content={"message": "Server error."},
            )
