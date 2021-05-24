from dataclasses import dataclass
from typing import Any

from injector import inject
from fastapi.responses import JSONResponse

@inject
@dataclass
class Responder():
    @staticmethod
    def send(data: Any, statusCode: int = 200, transformer = None):
        if not transformer:
            return JSONResponse(
                status_code=statusCode,
                content={"data": data}
            )

        data = transformer.handle(data)

        return JSONResponse(
            status_code=statusCode,
            content={"data": data}
        )
