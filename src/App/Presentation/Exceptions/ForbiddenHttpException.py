
from fastapi import Request
from fastapi.responses import JSONResponse
from src.Auth.Domain.Exceptions.ForbiddenException import ForbiddenException
from typing import Any


class ForbiddenHttpException:

    def __init__(self, app: Any):
        @app.exception_handler(ForbiddenException)
        async def forbidden_http_exception_handler(request: Request, exc: ForbiddenException):
            return JSONResponse(
                status_code=403,
                content={"message": "You do not have the access permissions."},
            )
