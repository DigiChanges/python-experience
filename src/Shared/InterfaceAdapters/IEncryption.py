from abc import ABC, abstractmethod


class IEncryption(ABC):

    @abstractmethod
    def compare(self, chain: str, chainHashed: str) -> bool:
        pass

    @abstractmethod
    def decrypt(self, chain: str) -> str:
        pass

    @abstractmethod
    def encrypt(self, chain: str) -> str:
        pass
