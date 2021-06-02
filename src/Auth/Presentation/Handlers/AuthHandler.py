from fastapi import APIRouter, Depends

from src.Auth.Domain.UseCases.LoginUseCase import LoginUseCase
from src.Auth.Domain.UseCases.PermissionUseCase import PermissionUseCase
from src.Auth.Presentation.Requests.AuthRequest import AuthRequest
from src.Auth.Presentation.Transformers.AuthTransformer import AuthTransformer
from src.Auth.Presentation.Transformers.PermissionTransformer import PermissionTransformer
from src.lazyInject import lazyInject
from src.Shared.Helpers.Responder import Responder
from src.User.Presentation.Requests.UserRepRequest import UserRepRequest
from src.User.Presentation.Transformers.UserTransformer import UserTransformer

router = APIRouter(
    prefix="/api/auth",
    responses={404: {"data": "Not found"}}
)

responder: Responder = lazyInject.get(Responder)

@router.post("/login")
async def login(request: AuthRequest):

    loginUseCase = LoginUseCase()
    data = loginUseCase.handle(request)

    return Responder.send(data, 201, AuthTransformer())

@router.get("/permissions")
async def permissions():

    permissionUseCase = PermissionUseCase()
    data = permissionUseCase.handle()

    return Responder.send(data, 200, PermissionTransformer())
