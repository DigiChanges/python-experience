from src.Shared.Helpers.Transformer import Transformer
from src.User.Domain.Entities.User import User

class UserTransformer(Transformer):
    # roleTransformer: RoleTransformer

    def __init__(self):
        super()
        # self.roleTransformer = RoleTransformer()

    def transform(self, user: User):
        return {
            "id": str(user.id),
            "firstName": user.firstName,
            "lastName": user.lastName,
            "email": user.email,
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

