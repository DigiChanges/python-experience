import re
from fastapi import Request
from src.Shared.Criteria.CriteriaRequest import CriteriaRequest
from src.Shared.InterfaceAdapters.ICriteriaPayload import ICriteriaPayload


def getParams(req: Request) -> ICriteriaPayload:
    params = {
        "pagination": {},
        "filter": {},
        "sort": {},
        "currentUrl": None
    }

    try:
        _query = dict(req.query_params)

        params["currentUrl"] = req.url

        for key in _query.keys():
            if "pagination" in key:
                rex = re.search(r"\[(.*?)\]", key)
                value = rex.group(1)

                params["pagination"][value] = _query.get(key)

            if "filter" in key:
                rex = re.search(r"\[(.*?)\]", key)
                value = rex.group(1)

                params["filter"][value] = _query.get(key)

            if "sort" in key:
                rex = re.search(r"\[(.*?)\]", key)
                value = rex.group(1)

                params["sort"][value] = _query.get(key)

    except Exception as e:
        raise e
    finally:
        return CriteriaRequest(params)