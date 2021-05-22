from pydantic import BaseModel
from src.IdPayload import IdPayload


class IdRequest(IdPayload, BaseModel):
    id: str

    def getId(self):
        return self.id

    def setId(self, id: str):
        self.id = id
