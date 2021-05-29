from mongoengine import Document, StringField, IntField, BooleanField, ListField


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
    permissions = ListField(StringField(max_length=30))

    def __str__(self):
        return (f"{self.firstName}, {self.lastName}, {self.email}, {self.password}, {self.birthday}, {self.documentType}, {self.documentNumber}, {self.gender}, {self.phone}, {self.country}, {self.address}, {self.enable}")