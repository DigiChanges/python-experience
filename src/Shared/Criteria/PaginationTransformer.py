from src.Shared.InterfaceAdapters.IPaginator import IPaginator


class PaginationTransformer():

    @staticmethod
    def transform(paginator: IPaginator):
        return {
            "currentUrl": paginator.getCurrentUrl(),
            "nextUrl": paginator.getNextUrl()
        }