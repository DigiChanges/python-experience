
from typing import Any

from fastapi import Request
from fastapi.responses import JSONResponse
from src.Auth.Domain.Exceptions.TokenNotFoundException import TokenNotFoundException


class TokenNotFoundHttpException:

    def __init__(self, app: Any):
        @app.exception_handler(TokenNotFoundException)
        async def token_not_found_http_exception_handler(request: Request, exc: TokenNotFoundException):
            return JSONResponse(
                status_code=403,
                content={"message": "Token not found."},
            )
