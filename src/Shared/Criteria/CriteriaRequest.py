from src.Shared.InterfaceAdapters.ICriteriaPayload import ICriteriaPayload


class CriteriaRequest(ICriteriaPayload):
    pagination: dict
    filter: dict
    sort: dict
    currentUrl: str

    def __init__(self, params: dict):
        self.pagination = params["pagination"]
        self.filter = params["filter"]
        self.sort = params["sort"]
        self.currentUrl = params["currentUrl"]

    def getPagination(self) -> dict:
        return self.pagination

    def getFilter(self) -> dict:
        return self.filter

    def getSort(self) -> dict:
        return self.sort

    def getCurrentUrl(self) -> str:
        return self.currentUrl