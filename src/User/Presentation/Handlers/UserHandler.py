from fastapi import APIRouter

from src.User.Presentation.Requests.UserUpdateRepRequest import UserUpdateRepRequest
from src.User.Presentation.Requests.UserRepRequest import UserRepRequest


router = APIRouter(
    prefix="/api/users",
    responses={404: {"data": "Not found"}}
)

class UserHandler():
    def __init__(self):
        self.responder = None

    @router.post("/")
    async def addUser(request: UserRepRequest):
        if request.passwordValidation():
            return {"data": 'Error'}

        return {"data": request.getFirstName()}

    @router.put("/{id}")
    async def updateUser(request: UserRepRequest, id: str):
        # result = UseCase(request, id)
        return {"data": request}

    @router.get("/{id}")
    async def getUser(id: int):
        return {"id": id}
