from src.Config.Permissions import Permissions

class PermissionUseCase:

    def handle(self):
        return Permissions.permissions()
