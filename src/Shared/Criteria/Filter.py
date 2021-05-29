from abc import abstractmethod
from typing import List, Any

from src.Shared.InterfaceAdapters.IFilter import IFilter


class Filter(IFilter):
    # private readonly filters: Map<string, any>;

    def __init__(self, request):
        pass
    #     this.filters = new Map<string, string>();
    #     let queryFilters: any = request.query.hasOwnProperty('filter') ? request.query.filter : [];
    #     let defaultFilters: any = this.getDefaultFilters();
    #     let keys = this.getFields();
    #
    #     defaultFilters.forEach((defaultFilter: any) => {
    #         const defaultKey: string = Object.keys(defaultFilter)[0];
    #         const defaultValue: string = defaultFilter[defaultKey];
    #
    #         this.filters.set(defaultKey, defaultValue);
    #     });
    #
    #     let newFilters = Object.keys(queryFilters).map((key: string) =>
    #     {
    #         const filter: any = request.query.filter;
    #
    #         return {
    #             [key]: filter[key]
    #         };
    #     }).filter((value => {
    #         const key = Object.keys(value)[0];
    #         return keys.includes(key) ? value : false;
    #     }));
    #
    #     newFilters.forEach((newFilter: any) => {
    #         const defaultKey: string = Object.keys(newFilter)[0];
    #         const defaultValue: string = newFilter[defaultKey];
    #
    #         this.filters.set(defaultKey, defaultValue);
    #     });
    # }

    def get(self, key: str) -> str:
        pass # return this.filters.has(key) ? this.filters.get(key) : '';


    def getArray(self):
        pass # return this.filters.entries()

    def has(sel, key: str) -> bool:
        pass # return this.filters.has(key)

    def isEmpty(self) -> bool:
        pass # return this.filters.size === 0;

    def values(self): # Map<string, any>
        pass # return this.filters;

    @abstractmethod
    def getFields(self) -> List: # any[];
        pass

    @abstractmethod
    def getDefaultFilters(self) -> Any:
        pass

# export class PaginatorTransformer extends Transformer
# {
#     public transform(paginator: IPaginator)
#     {
#         return {
#             total: paginator.getTotal(),
#             currentUrl: paginator.getCurrentUrl(),
#             nextUrl: paginator.getNextUrl()
#         };
#     }
# }