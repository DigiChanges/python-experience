from abc import ABC, abstractmethod

class IdPayload(ABC):
    def getId(self):
        pass

    def setId(self, id: str):
        pass