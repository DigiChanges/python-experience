from typing import Any
from src.Shared.InterfaceAdapters.IFilter import IFilter


class Filter(IFilter):
    _filters: dict

    def __init__(self, filter: dict):
        self._filters = filter

        defaultFilters: Any = self.getDefaultFilters()

        for valueKey in defaultFilters:
            self._filters.update(valueKey)

    def get(self, key: str) -> str:
        return self._filters.get(key) if self.has(key) else None

    def has(self, key: str) -> bool:
        return key in self._filters

    def isEmpty(self) -> bool:
        return True if self._filters else False

    def values(self) -> dict:
        return self._filters
