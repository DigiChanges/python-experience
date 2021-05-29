
from typing import Any

from fastapi import Request
from fastapi.responses import JSONResponse
from src.User.Domain.Exceptions.UserDisabledException import UserDisabledException


class UserDisabledHttpException:

    def __init__(self, app: Any):
        @app.exception_handler(UserDisabledException)
        async def user_disabled_http_exception_handler(request: Request, exc: UserDisabledException):
            return JSONResponse(
                status_code=401,
                content={"message": "Your user is disable."},
            )
