
from typing import List


class Permissions:
    ALL: str = 'all'

    # AUTH
    GET_PERMISSIONS: str = 'getPermissions'

    # USERS
    USERS_ASSIGN_ROLE: str = 'usersAssignRole'
    USERS_CHANGE_USER_PASSWORD: str = 'usersChangeUserPassword'
    USERS_DELETE: str = 'usersDelete'
    USERS_LIST: str = 'usersList'
    USERS_SAVE: str = 'usersSave'
    USERS_SHOW: str = 'usersShow'
    USERS_UPDATE: str = 'usersUpdate'

    # ROLES
    ROLES_DELETE: str = 'rolesDelete'
    ROLES_LIST: str = 'rolesList'
    ROLES_SAVE: str = 'rolesSave'
    ROLES_SHOW: str = 'rolesShow'
    ROLES_UPDATE: str = 'rolesUpdate'

    def permissions() -> List[str]:
        return [

            f"{Permissions.GET_PERMISSIONS}",

            f"{Permissions.USERS_ASSIGN_ROLE}",
            f"{Permissions.USERS_CHANGE_USER_PASSWORD}",
            f"{Permissions.USERS_DELETE}",
            f"{Permissions.USERS_LIST}",
            f"{Permissions.USERS_SAVE}",
            f"{Permissions.USERS_SHOW}",
            f"{Permissions.USERS_UPDATE}",

            f"{Permissions.ROLES_DELETE}",
            f"{Permissions.ROLES_LIST}",
            f"{Permissions.ROLES_SAVE}",
            f"{Permissions.ROLES_SHOW}",
            f"{Permissions.ROLES_UPDATE}",

        ]