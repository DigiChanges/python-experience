from typing import List
from pydantic import BaseModel
from src.User.InterfaceAdapters.Payloads.UserRepPayload import UserRepPayload


class UserRepRequest(UserRepPayload, BaseModel):
    firstName: str
    lastName: str
    email: str
    password: str
    passwordConfirmation: str
    birthday: str
    documentType: str
    documentNumber: int
    gender: str
    phone: str
    country: str
    address: str
    enable: bool
    permissions: List[str] = []

    def passwordValidation(self):
        return self.password != self.passwordConfirmation

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getEmail(self):
        return self.email

    def getPassword(self):
        return self.password
