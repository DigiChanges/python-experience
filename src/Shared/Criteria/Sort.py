from typing import Any, List

from src.Shared.InterfaceAdapters.ISort import ISort


class Sort(ISort):
    # private readonly sorts: Map<string, string>;

    # constructor(request: express.Request)
    #     // TODO: Remove logic from constructor
    #     this.sorts = new Map<string, string>();
    #     let sorts: any = request.query.hasOwnProperty('sort') ? request.query.sort : [];
    #     let keys = this.getFields();
    #
    #     let newSorts = Object.keys(sorts).map((key: string) =>
    #     {
    #         const sort: any = request.query.sort;
    #
    #         return {
    #             [key]: sort[key]
    #         };
    #     }).filter((value => {
    #         const key = Object.keys(value)[0];
    #         return keys.includes(key) ? value : false;
    #     }));
    #
    #     newSorts.forEach((newSort: any) => {
    #         const defaultKey: string = Object.keys(newSort)[0];
    #         const defaultValue: string = newSort[defaultKey];
    #
    #         this.sorts.set(defaultKey, defaultValue);
    #     });
    #
    #     let defaultSorts = this.getDefaultSorts();
    #
    #     if (this.sorts.size === 0)
    #     {
    #         defaultSorts.forEach((defaultSort: any) =>
    #         {
    #             const defaultKey: string = Object.keys(defaultSort)[0];
    #             const defaultValue: string = defaultSort[defaultKey];
    #
    #             this.sorts.set(defaultKey, defaultValue);
    #         });
    #     }
    # }

    def get(self) -> List: # Map<string, string>
        pass # return this.sorts;

    def getFields(self) -> Any:
        pass

    def getDefaultSorts(self) -> Any:
        pass