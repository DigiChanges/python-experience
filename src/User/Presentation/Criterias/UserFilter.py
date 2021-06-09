from typing import Any
from src.Shared.Criteria.Filter import Filter


class UserFilter(Filter):
    EMAIL: str = 'email'
    FIRST_NAME: str = 'firstName'
    ENABLE: str = 'enable'
    IS_SUPER_ADMIN: str = 'isSuperAdmin'

    def __init__(self, filter):
        super().__init__(filter)

    def getFields(self) -> Any:
        return [
            UserFilter.EMAIL,
            UserFilter.FIRST_NAME,
            UserFilter.ENABLE,
            UserFilter.IS_SUPER_ADMIN
        ]

    def getDefaultFilters(self) -> Any:
        return [
            {f"{UserFilter.IS_SUPER_ADMIN}": False}
        ]
