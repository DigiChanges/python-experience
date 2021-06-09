from src.Shared.Helpers.Transformer import Transformer
from src.Role.Domain.Entities.Role import Role

class RoleTransformer(Transformer):

    def __init__(self):
        super()

    def transform(self, role: Role):
        return {
            "id": str(role.id),
            "name": role.name,
            "slug": role.slug,
            "enable": role.enable,
            "permissions": role.permissions
        }

