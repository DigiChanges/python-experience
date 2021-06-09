from fastapi import APIRouter, Depends
from src.App.Presentation.ObjectIdStr import ObjectIdStr
from src.Auth.AuthBearer import JWTBearer
from src.Config.Permissions import Permissions
from src.lazyInject import lazyInject
from src.Role.Domain.UseCases.GetOneRoleUseCase import GetOneRoleUseCase
from src.Role.Domain.UseCases.SaveRoleUseCase import SaveRoleUseCase
from src.Role.Domain.UseCases.UpdateRoleUseCase import UpdateRoleUseCase
from src.Role.Presentation.Requests.RoleRepRequest import RoleRepRequest
from src.Role.Presentation.Requests.RoleUpdateRepRequest import RoleUpdateRepRequest
from src.Role.Presentation.Transformers.RoleTransformer import RoleTransformer
from src.Shared.Helpers.Responder import Responder


router = APIRouter(
    prefix="/api/roles",
    responses={404: {"data": "Not found"}}
)

responder: Responder = lazyInject.get(Responder)

@router.post("/", dependencies=[Depends(JWTBearer(Permissions.ROLES_SAVE))])
async def addRole(request: RoleRepRequest):

    useCase = SaveRoleUseCase()
    data = useCase.handle(request)

    return Responder.send(data, 201, RoleTransformer())

@router.put("/{id}", dependencies=[Depends(JWTBearer(Permissions.ROLES_UPDATE))])
async def updateRole(request: RoleUpdateRepRequest, id: ObjectIdStr):
    useCase = UpdateRoleUseCase()
    data = useCase.handle(request, id)

    return Responder.send(data, 201, RoleTransformer())

@router.get("/{id}", dependencies=[Depends(JWTBearer(Permissions.ROLES_SHOW))])
async def getRole(id: ObjectIdStr):
    useCase = GetOneRoleUseCase()
    data = useCase.handle(id)

    return Responder.send(data, 200, RoleTransformer())
