from dataclasses import dataclass
from typing import Any

from injector import inject
from fastapi.responses import JSONResponse

from src.Shared.Criteria.PaginationTransformer import PaginationTransformer
from src.Shared.InterfaceAdapters.IPaginator import IPaginator



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

    @staticmethod
    def paginate(paginator: IPaginator, statusCode: int = 200, transformer = None):
        data = paginator.paginate()
        response = {"data": None}

        if transformer:
            data = transformer.handle(data)

        if paginator.getExist():
            paginationTransformer = PaginationTransformer.transform(paginator)
            response.update({"pagination": paginationTransformer})

        response["data"] = data

        return JSONResponse(
             status_code=statusCode,
             content=response
        )
