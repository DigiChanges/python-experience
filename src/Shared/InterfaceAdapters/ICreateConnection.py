from abc import ABC, abstractmethod


class ICreateConnection(ABC):

    @abstractmethod
    def init(self):
        pass

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def close(self):
        pass