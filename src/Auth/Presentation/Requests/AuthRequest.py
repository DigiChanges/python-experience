from pydantic import BaseModel
from src.Auth.InterfaceAdapters.Payloads.AuthPayload import AuthPayload
from src.Auth.Presentation.Requests.Examples.AuthSchema import OpenApi


class AuthRequest(AuthPayload, BaseModel):
    email: str
    password: str

    def getEmail(self) -> str:
        return self.email

    def getPassword(self) -> str:
        return self.password

    class Config(OpenApi):
        pass