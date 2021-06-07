from mongoengine import Document, StringField, BooleanField, ListField


class Role(Document):
    name = StringField()
    slug = StringField()
    enable = BooleanField()
    permissions = ListField(StringField(max_length=30))

    def __str__(self):
        return (f"{self.name}, {self.slug}, {self.enable}")