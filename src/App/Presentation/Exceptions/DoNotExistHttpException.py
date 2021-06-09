
from typing import Any

from fastapi import Request
from fastapi.responses import JSONResponse
from mongoengine.errors import DoesNotExist

class DoNotExistHttpException:

    def __init__(self, app: Any):
        @app.exception_handler(DoesNotExist)
        async def do_not_exist_http_exception_handler(request: Request, exc: DoesNotExist):
            return JSONResponse(
                status_code=400,
                content={"message": str(exc)},
            )
