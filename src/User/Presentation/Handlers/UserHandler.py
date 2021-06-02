from src.Config.Permissions import Permissions
from src.Auth.AuthBearer import JWTBearer
from fastapi import APIRouter, Depends

from src.Shared.Helpers.Responder import Responder
from src.User.Domain.UseCases.GetOneUserUseCase import GetOneUserUseCase
from src.User.Domain.UseCases.ListUserUseCase import ListUserUseCase
from src.User.Domain.UseCases.SaveUserUseCase import SaveUserUseCase
from src.User.Domain.UseCases.UpdateUserUseCase import UpdateUserUseCase
from src.User.Presentation.Requests.UserRepRequest import UserRepRequest
from src.User.Presentation.Requests.UserUpdateRepRequest import UserUpdateRepRequest
from src.User.Presentation.Transformers.UserTransformer import UserTransformer
from src.lazyInject import lazyInject

router = APIRouter(
    prefix="/api/users",
    responses={404: {"data": "Not found"}}
)

responder: Responder = lazyInject.get(Responder)

@router.post("/")
# @router.post("/", dependencies=[Depends(JWTBearer())])
async def addUser(request: UserRepRequest):

    useCase = SaveUserUseCase()
    data = useCase.handle(request)

    return Responder.send(data, 201, UserTransformer())

@router.put("/{id}", dependencies=[Depends(JWTBearer(Permissions.USERS_UPDATE))])
async def updateUser(request: UserUpdateRepRequest, id: str):
    useCase = UpdateUserUseCase()
    data = useCase.handle(request, id)

    return Responder.send(data, 201, UserTransformer())

@router.get("/{id}", dependencies=[Depends(JWTBearer(Permissions.USERS_SHOW))])
async def getUser(id: str):
    useCase = GetOneUserUseCase()
    data = useCase.handle(id)

    return Responder.send(data, 200, UserTransformer())

@router.get("/")
async def getUsers(pagination):

    print('pagination')
    print(pagination)

    useCase = ListUserUseCase()
    data = useCase.handle()

    return Responder.send(data, 200, UserTransformer())
