from pydantic import BaseModel

from src.IdRequest import IdRequest
from src.User.InterfaceAdapters.Payloads.UserUpdateRepPayload import UserUpdateRepPayload
from src.User.Presentation.Requests.UserRepRequest import UserRepRequest


class UserUpdateRepRequest(UserRepRequest, IdRequest, UserUpdateRepPayload, BaseModel):
    pass
