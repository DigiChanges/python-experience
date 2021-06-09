from src.Shared.InterfaceAdapters.ISort import ISort


class Sort(ISort):
    _sorts: dict
    _res: dict

    def __init__(self, sorts: dict):
        self._sorts = self.getDefaultSorts()
        self._res = {}

        self._sorts.update(sorts)
        fields = self.getFields()

        for field in fields:
            if field in sorts:
                self._res[field] = sorts[field]

    def get(self) -> dict:
        return self._res
