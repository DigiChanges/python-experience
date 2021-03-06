from abc import ABC
from typing import List


class IUserDomain(ABC):
    firstName: str
    lastName: str
    email: str
    password: str
    birthday: str
    documentType: str
    documentNumber: int
    gender: str
    phone: str
    country: str
    address: str
    enable: bool
    permissions: List
