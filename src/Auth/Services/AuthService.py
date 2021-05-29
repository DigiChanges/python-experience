import time
from typing import Any, Dict, List

from jose import jwt
from src.Auth.InterfaceAdapters.IAuthService import IAuthService
from src.Shared.Config import config


class AuthService (IAuthService):

    def decodeToken(self, token: str) -> Dict[str, str]:
        secret: str = config.get('jwt', {}).get('secret')
        algorithm: str = config.get('jwt', {}).get('algorithm')
        try:
            decoded_token = jwt.decode(token, secret, algorithms=[algorithm])
            return decoded_token if decoded_token["exp"] >= time.time() else None
        except:
            return {}

    def getPermissions(user: Any) -> List[str]:
        raise Exception("getPermissions not implemented")

    def validatePermissions(permissions: List[str]) -> None:
        raise Exception("getPermissions not implemented")