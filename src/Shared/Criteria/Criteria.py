from src.Shared.InterfaceAdapters.ICriteria import ICriteria
from src.Shared.InterfaceAdapters.IFilter import IFilter
from src.Shared.InterfaceAdapters.IPagination import IPagination
from src.Shared.InterfaceAdapters.ISort import ISort


class Criteria(ICriteria):

    pagination: IPagination
    filter: IFilter
    sort: ISort

    def __init__(self, pagination: IPagination, filter: IFilter, sort: ISort):
        self.pagination = pagination
        self.filter = filter
        self.sort = sort

    def getPagination(self) -> IPagination:
        return self.pagination

    def getFilter(self) -> IFilter:
        return self.filter

    def getSort(self) -> ISort:
        return self.sort
