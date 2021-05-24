
from typing import Any

from fastapi import Request
from fastapi.responses import JSONResponse
from src.Shared.Exceptions.DecryptForbiddenException import DecryptForbiddenException


class DecryptForbiddenHttpException:

    def __init__(self, app: Any):
        @app.exception_handler(DecryptForbiddenException)
        async def http_decrypt_forbidden_http_exception_handler(request: Request, exc: DecryptForbiddenException):
            return JSONResponse(
                status_code=401,
                content={"message": "Decrypt forbidden"},
            )
