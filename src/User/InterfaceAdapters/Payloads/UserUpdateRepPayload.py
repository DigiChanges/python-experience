from abc import ABC, abstractmethod
from typing import List


class UserUpdateRepPayload(ABC):
    firstName: str
    lastName: str
    email: str
    birthday: str
    documentType: str
    documentNumber: int
    gender: str
    phone: str
    country: str
    address: str
    enable: bool
    permissions: List[str]

    @abstractmethod
    def getFirstName(self):
        pass

    @abstractmethod
    def getLastName(self):
        pass

    @abstractmethod
    def getEmail(self):
        pass

    @abstractmethod
    def getBirthday(self):
        pass

    @abstractmethod
    def getDocumentType(self):
        pass

    @abstractmethod
    def getDocumentNumber(self):
        pass

    @abstractmethod
    def getGender(self):
        pass

    @abstractmethod
    def getPhone(self):
        pass

    @abstractmethod
    def getCountry(self):
        pass

    @abstractmethod
    def getAddress(self):
        pass

    @abstractmethod
    def getEnable(self):
        pass

    @abstractmethod
    def getPermissions(self):
        pass
