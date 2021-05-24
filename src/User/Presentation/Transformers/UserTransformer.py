from src.Shared.Helpers.Transformer import Transformer
from src.User.Infrastructure.UserDocument import UserDocument

class UserTransformer(Transformer):
    # roleTransformer: RoleTransformer

    def __init__(self):
        super()
        # self.roleTransformer = RoleTransformer()

    def transform(self, user: UserDocument):
        return {
            "id": str(user.id),
            "firstName": user.firstName,
            "lastName": user.lastName,
            "email": user.email,
            "password": user.password,
            "birthday": user.birthday,
            "documentType": user.documentType,
            "documentNumber": user.documentNumber,
            "gender": user.gender,
            "phone": user.phone,
            "country": user.country,
            "address": user.address,
            "enable": user.enable,
            "permissions": user.permissions
        }

