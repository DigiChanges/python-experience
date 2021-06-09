from functools import reduce
from injector import inject
from dataclasses import dataclass
from mongoengine import Q

from src.Shared.Criteria.MongoPaginator import MongoPaginator
from src.Shared.InterfaceAdapters.ICriteria import ICriteria
from src.User.Domain.Entities.User import User
from src.User.InterfaceAdapters.IUserRepository import IUserRepository
from src.User.Presentation.Criterias.UserFilter import UserFilter


@inject
@dataclass
class UserRepository(IUserRepository):
    def save(self, element):
        return element.save()

    def getOne(self, id: str):
        return User.objects.get(id=id)

    def list(self, criteria: ICriteria):
        queryBuilder = User.objects
        filter = criteria.getFilter()

        if filter.has(UserFilter.EMAIL):
            filters = filter.get(UserFilter.EMAIL)
            query = reduce(lambda q1, q2: q1 | q2,
               map(lambda email: Q(email__icontains=email), filters))
            queryBuilder = queryBuilder(query)

        if filter.has(UserFilter.FIRST_NAME):
            firstName = filter.get(UserFilter.FIRST_NAME)
            queryBuilder = queryBuilder(firstName=f"{firstName}").filter

        return MongoPaginator(queryBuilder, criteria)

    def delete(self, id: str):
        return User.objects.delete(id=id)

    def getOneByEmail(self, email: str):
        return User.objects.get(email=email)

    def getOneByConfirmationToken(self, confirmationToken: str):
        return User.objects.get(confirmationToken=confirmationToken)
