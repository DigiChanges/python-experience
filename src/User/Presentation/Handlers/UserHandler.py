from fastapi import APIRouter

from src.Shared.Helpers.Responder import Responder
from src.User.Domain.UseCases.SaveUserUseCase import SaveUserUseCase
from src.User.Presentation.Requests.UserRepRequest import UserRepRequest
from src.User.Presentation.Transformers.UserTransformer import UserTransformer
from src.lazyInject import lazyInject

router = APIRouter(
    prefix="/api/users",
    responses={404: {"data": "Not found"}}
)

responder: Responder = lazyInject.get(Responder)

@router.post("/")
async def addUser(request: UserRepRequest):
    if request.passwordValidation(): # Change to raise error exception on UseCase
        return {"data": 'Error'}

    useCase = SaveUserUseCase()
    data = useCase.handle(request)

    return Responder.send(data, 201, UserTransformer())

@router.put("/{id}")
async def updateUser(request: UserRepRequest, id: str):
    return {"data": request}

@router.get("/{id}")
async def getUser(id: int):
    return {"id": id}
