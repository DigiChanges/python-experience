
from typing import Any

from fastapi import Request
from fastapi.responses import JSONResponse


class ErrorHttpException:

    def __init__(self, app: Any):
        @app.exception_handler(FileNotFoundError)
        async def http_file_http_exception_handler(request: Request, exc: FileNotFoundError):
            return JSONResponse(
                status_code=500,
                content={"message": "Filesystem error."},
            )

        @app.exception_handler(Exception)
        async def http_general_http_exception_handler(request: Request, exc: Exception):
            return JSONResponse(
                status_code=500,
                content={"message": "Server error."},
            )
