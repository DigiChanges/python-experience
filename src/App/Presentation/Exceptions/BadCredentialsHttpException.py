
from typing import Any

from fastapi import Request
from fastapi.responses import JSONResponse
from src.Auth.Domain.Exceptions.BadCredentialsException import BadCredentialsException


class BadCredentialsHttpException:

    def __init__(self, app: Any):
        @app.exception_handler(BadCredentialsException)
        async def bad_credentials_http_exception_handler(request: Request, exc: BadCredentialsException):
            return JSONResponse(
                status_code=401,
                content={"message": "Error credentials."},
            )
