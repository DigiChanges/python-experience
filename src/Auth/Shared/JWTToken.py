
from dataclasses import dataclass
from typing import Any, Dict
from jose import JWTError, jwt
from pydantic.main import BaseModel
from src.Shared.Config import config


class JWTToken():
    expires: int
    hash: str
    user: Any
    payload: Dict[str, str]

    def __init__(self, expires,  user) -> None:

        self.expires = expires
        self.user = user

        self.payload = {
            "iss": config["jwt"]["iss"],
            "aud": config["jwt"]["aud"],
            "sub": self.user.email,
            "iat": self.expires,
            "userId": self.user.id,
            "email": self.user.email
        }

        self.hash = jwt.encode(self.payload, config["jwt"]["secret"], algorithm=config["jwt"]["algorithm"])

    def getExpires(self) -> int:
        return self.expires

    def getHash(self) -> str:
        return self.hash

    def getPayload(self) -> Dict[str, str]:
        return self.payload

    def getUser(self) -> Any:
        return self.user