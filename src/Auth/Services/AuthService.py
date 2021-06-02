from src.User.Domain.Entities.User import User
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

    def getPermissions(self, user: User) -> List[str]:
        permissions = user.permissions
        # roles = user.roles TODO: get roles array entity from user entity
        # iterate roles, get permissions, add to permissions list
        return set(permissions)


    def validatePermissions(self, permissions: List[str]) -> None:
        raise Exception("getPermissions not implemented")