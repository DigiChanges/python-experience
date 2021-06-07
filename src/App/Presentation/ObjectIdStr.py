from bson import ObjectId
from mongoengine.base.fields import ObjectIdField


class ObjectIdStr(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        resultIsValid = ObjectIdField.is_valid(str(v))
        print('>>> resultIsValid')
        print(resultIsValid)
        if not ObjectIdField.is_valid(str(v)):
            return ValueError(f"Not a valid ObjectId: {v}")
        return ObjectId(str(v))