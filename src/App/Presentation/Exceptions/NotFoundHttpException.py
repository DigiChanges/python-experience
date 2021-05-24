
from fastapi import Request
from fastapi.responses import JSONResponse
from src.Shared.Exceptions.NotFoundException import NotFoundException
from typing import Any


class NotFoundHttpException:

    def __init__(self, app: Any):
        @app.exception_handler(NotFoundException)
        async def http_not_found_exception_handler(request: Request, exc: NotFoundException):
            return JSONResponse(
                status_code=400,
                content={"message": f"{exc.name} not found."},
            )
