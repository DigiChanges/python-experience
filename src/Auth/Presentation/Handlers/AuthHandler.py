from src.Auth.Domain.UseCases.LoginUseCase import LoginUseCase
from src.Auth.Presentation.Requests.AuthRequest import AuthRequest
from src.Auth.AuthBearer import JWTBearer
from fastapi import APIRouter, Depends

from src.Shared.Helpers.Responder import Responder
from src.User.Presentation.Requests.UserRepRequest import UserRepRequest
from src.User.Presentation.Transformers.UserTransformer import UserTransformer
from src.Auth.Presentation.Transformers.AuthTransformer import AuthTransformer
from src.lazyInject import lazyInject

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
