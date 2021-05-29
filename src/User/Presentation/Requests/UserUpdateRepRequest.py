from typing import List
from pydantic import BaseModel
from src.User.InterfaceAdapters.Payloads.UserUpdateRepPayload import UserUpdateRepPayload


class UserUpdateRepRequest(UserUpdateRepPayload, BaseModel):
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
    permissions: List[str] = []

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getEmail(self):
        return self.email

    def getBirthday(self):
        return self.birthday

    def getDocumentType(self):
        return self.documentType

    def getDocumentNumber(self):
        return self.documentNumber

    def getGender(self):
        return self.gender

    def getPhone(self):
        return self.phone

    def getCountry(self):
        return self.country

    def getAddress(self):
        return self.address

    def getEnable(self):
        return self.enable

    def getPermissions(self):
        return self.permissions
