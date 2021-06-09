from src.Shared.InterfaceAdapters.IPagination import IPagination


class Pagination(IPagination):
    limit: int
    offset: int
    exist: bool
    currentUrl: str

    def __init__(self, pagination: dict, currentUrl: str):
        self.limit = int(pagination["limit"]) if pagination else 10
        self.offset = int(pagination["offset"]) if pagination else 0
        self.currentUrl = currentUrl
        self.exist = True if pagination else False

    def getLimit(self) -> int:
        return self.limit

    def getOffset(self) -> int:
        return self.offset

    def getCurrentUrl(self) -> str:
        return self.currentUrl.__str__()

    def getNextUrl(self) -> str:
        newOffset = self.offset + self.limit
        return self.currentUrl.__str__().replace(f'[offset]={self.offset}', f'[offset]={newOffset}')


    def getExist(self) -> bool:
        return self.exist
