from bson import ObjectId
from fastapi import HTTPException


class ObjectIdStr(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):

        if not ObjectId.is_valid(str(v)):
            raise HTTPException(422, f"Not a valid ObjectId: {v}")

        return ObjectId(str(v))