from typing import List
from pydantic import BaseModel

class User(BaseModel):
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
    permissions: List[str] = []

    def __init__(self, firstName, lastName, email, password, birthday, documentType, documentNumber, gender, phone, country, address, permissions):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password
        self.birthday = birthday
        self.documentType = documentType
        self.documentNumber = documentNumber
        self.gender = gender
        self.phone = phone
        self.country = country
        self.address = address
        self.permissions = permissions
