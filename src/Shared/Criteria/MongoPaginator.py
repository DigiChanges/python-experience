from typing import Any

from src.Shared.InterfaceAdapters.ICriteria import ICriteria
from src.Shared.InterfaceAdapters.IFilter import IFilter
from src.Shared.InterfaceAdapters.IPagination import IPagination
from src.Shared.InterfaceAdapters.IPaginator import IPaginator
from src.Shared.InterfaceAdapters.ISort import ISort


class MongoPaginator(IPaginator):
    qQuerySetManager: Any
    _filter: IFilter
    _sort: ISort
    _pagination: IPagination
    _total: int
    _helper: Any

    def __init__(self, querySetManager: Any, criteria: ICriteria, helper: Any = None):
        self.querySetManager = querySetManager
        self.filter = criteria.getFilter()
        self.sort = criteria.getSort()
        self.pagination = criteria.getPagination()
        self.helper = helper

    def getTotal(self) -> int:
        return self._total

    def getCurrentUrl(self) -> str:
        return self.pagination.getCurrentUrl()

    # TODO: Don't show next url when it doesnt exist more data
    def getNextUrl(self) -> str:
        return self.pagination.getNextUrl()

    def paginate(self) -> Any:
        # TODO: Add filter logic

        self._addOrderBy()
        # self.total = data.count()

        # TODO: Helper
        # data = self.querySetManager()
        # if (self.helper):
        #     data = self.helper(data)

        exist = self.pagination.getExist()

        if (exist):
            return self.querySetManager().skip(self.pagination.getOffset()).limit(self.pagination.getLimit())

        return self.querySetManager()

    def getExist(self) -> bool:
        return self.pagination.getExist()

    def _addOrderBy(self) -> None:
        sorts = self.sort.get()
        _objectSort = {}

        for sort in sorts:
            valueSort = sorts[sort].lower()
            if valueSort == 'asc':
                self.querySetManager = self.querySetManager().order_by(f'+{sort}').filter
            else:
                self.querySetManager = self.querySetManager().order_by(f'-{sort}').filter
