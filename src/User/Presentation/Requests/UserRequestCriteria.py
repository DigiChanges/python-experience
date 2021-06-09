from src.Shared.Criteria.Criteria import Criteria
from src.Shared.Criteria.CriteriaRequest import CriteriaRequest
from src.Shared.Criteria.Pagination import Pagination
from src.User.Presentation.Criterias.UserFilter import UserFilter
from src.User.Presentation.Criterias.UserSort import UserSort


class UserRequestCriteria(Criteria):
    def __init__(self, req: CriteriaRequest):
        super().__init__(Pagination(req.getPagination(), req.getCurrentUrl()), UserFilter(req.getFilter()), UserSort(req.getSort()))
