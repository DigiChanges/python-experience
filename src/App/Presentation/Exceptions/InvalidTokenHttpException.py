
from typing import Any

from fastapi import Request
from fastapi.responses import JSONResponse
from src.Auth.Domain.Exceptions.InvalidTokenException import InvalidTokenException


class InvalidTokenHttpException:

    def __init__(self, app: Any):
        @app.exception_handler(InvalidTokenException)
        async def invalid_token_http_exception_handler(request: Request, exc: InvalidTokenException):
            return JSONResponse(
                status_code=403,
                content={"message": "Invalid token."},
            )
