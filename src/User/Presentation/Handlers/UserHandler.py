from fastapi import APIRouter

from src.Shared.Responder import Responder
from src.User.Domain.UseCases.SaveUserUseCase import SaveUserUseCase
from src.User.Presentation.Requests.UserRepRequest import UserRepRequest
from src.lazyInject import lazyInject

router = APIRouter(
    prefix="/api/users",
    responses={404: {"data": "Not found"}}
)

responder: Responder = lazyInject.get(Responder)

@router.post("/")
async def addUser(request: UserRepRequest):
    if request.passwordValidation():
        return {"data": 'Error'}

    useCase = SaveUserUseCase()
    data = useCase.handle(request)

    return {"data": data}

@router.put("/{id}")
async def updateUser(request: UserRepRequest, id: str):
    return {"data": request}

@router.get("/{id}")
async def getUser(id: int):
    return {"id": id, 'res': responder.send()}
