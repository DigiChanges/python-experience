from src.Auth.InterfaceAdapters.IToken import IToken
from src.Shared.Helpers.Transformer import Transformer

class AuthTransformer(Transformer):
    # roleTransformer: RoleTransformer

    def __init__(self):
        super()
        # self.authService = AuthService()

    def transform(self, token: IToken):
        user = token.getUser()

        return {
            "user": {
                "id": user.id,
                "firstName": user.firstName,
                "email": user.email
            },
            "token": token.getHash()
        }

