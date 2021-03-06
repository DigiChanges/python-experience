from mongoengine import Document, StringField, IntField, BooleanField, ListField
from src.Role.Domain.Entities.Role import Role
from typing import List


class User(Document):
    firstName = StringField()
    lastName = StringField()
    email = StringField()
    password = StringField()
    birthday = StringField()
    documentType = StringField()
    documentNumber = IntField()
    gender = StringField()
    phone = StringField()
    country = StringField()
    address = StringField()
    enable = BooleanField()
    isSuperAdmin = BooleanField()
    permissions = ListField(StringField(max_length=30))
    roles = ListField(StringField(max_length=30))

    def clearRoles(self) -> None:
        self.roles: List([str]) = []

    def getRoles(self) -> List:
        return self.roles

    def setRole(self, role: Role) -> None:
        roleId = str(role.id)
        return self.roles.append(roleId)

    def __str__(self):
        return (f"{self.firstName}, {self.lastName}, {self.email}, {self.password}, {self.birthday}, {self.documentType}, {self.documentNumber}, {self.gender}, {self.phone}, {self.country}, {self.address}, {self.enable}")