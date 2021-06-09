from typing import List
from src.Shared.Criteria.Sort import Sort


class UserSort(Sort):
    EMAIL: str = 'email'

    def __init__(self, sort):
        super().__init__(sort)

    def getFields(self) -> List[str]:
        return [
            UserSort.EMAIL,
        ]

    def getDefaultSorts(self) -> dict:
        return {
            f"{UserSort.EMAIL}": "asc"
        }
