
from typing import Any, Dict
from jose import jwt
from src.User.Domain.Entities.User import User
from src.Shared.Config import config


class JWTToken():
    expires: int
    hash: str
    user: Any
    payload: Dict[str, str]

    def __init__(self, expires,  user: User) -> None:

        self.expires = expires
        self.user: User = user

        self.payload = {
            "sub": self.user.email,
            "userId": str(self.user.id),
            "email": self.user.email,
            "exp": expires
        }

        secret = config.get("jwt", {}).get("secret")
        algorithm = config.get("jwt", {}).get("algorithm")

        token = jwt.encode(self.payload, secret, algorithm=algorithm)
        self.hash = token

    def getExpires(self) -> int:
        return self.expires

    def getHash(self) -> str:
        return self.hash

    def getPayload(self) -> Dict[str, str]:
        return self.payload

    def getUser(self) -> Any:
        return self.user