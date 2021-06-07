from src.App.Presentation.ObjectIdStr import ObjectIdStr
from typing import Optional
from src.Config.Permissions import Permissions
from src.Auth.AuthBearer import JWTBearer
from fastapi import APIRouter, Depends

from pydantic import Field
from src.Shared.Helpers.Responder import Responder
from src.Role.Domain.UseCases.GetOneRoleUseCase import GetOneRoleUseCase
from src.Role.Domain.UseCases.ListRoleUseCase import ListRoleUseCase
from src.Role.Domain.UseCases.SaveRoleUseCase import SaveRoleUseCase
from src.Role.Domain.UseCases.UpdateRoleUseCase import UpdateRoleUseCase
from src.Role.Presentation.Requests.RoleRepRequest import RoleRepRequest
from src.Role.Presentation.Requests.RoleUpdateRepRequest import RoleUpdateRepRequest
from src.Role.Presentation.Transformers.RoleTransformer import RoleTransformer
from src.lazyInject import lazyInject

router = APIRouter(
    prefix="/api/roles",
    responses={404: {"data": "Not found"}}
)

responder: Responder = lazyInject.get(Responder)

@router.post("/")
# @router.post("/", dependencies=[Depends(JWTBearer())])
async def addRole(request: RoleRepRequest):

    useCase = SaveRoleUseCase()
    data = useCase.handle(request)

    return Responder.send(data, 201, RoleTransformer())

@router.put("/{id}", dependencies=[Depends(JWTBearer(Permissions.ROLES_UPDATE))])
async def updateRole(request: RoleUpdateRepRequest, id: str):
    useCase = UpdateRoleUseCase()
    data = useCase.handle(request, id)

    return Responder.send(data, 201, RoleTransformer())


@router.get("/{id}", dependencies=[Depends(JWTBearer(Permissions.ROLES_SHOW))])
async def getRole(id: Optional[ObjectIdStr] = Field(..., alias="_id")):
    useCase = GetOneRoleUseCase()
    data = useCase.handle(id)

    return Responder.send(data, 200, RoleTransformer())

@router.get("/")
async def getRoles(pagination):

    print('pagination')
    print(pagination)

    useCase = ListRoleUseCase()
    data = useCase.handle()

    return Responder.send(data, 200, RoleTransformer())
