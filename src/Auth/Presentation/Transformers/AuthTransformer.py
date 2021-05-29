from typing import Dict
from src.Auth.InterfaceAdapters.IToken import IToken
from src.Shared.Helpers.Transformer import Transformer

class AuthTransformer(Transformer):

    def __init__(self):
        super()

    def transform(self, token: IToken) -> Dict[str, str] :
        user = token.getUser()
        return {
            "user": {
                "id": str(user.id),
                "firstName": user.firstName,
                "lastName": user.lastName,
                "email": user.email,
                "enable": user.enable,
                # TODO: add authService getPermissions
                "permissions": user.permissions,
                # TODO: add role transformer 
            },
            "token": token.getHash()
        }

