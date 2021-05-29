from passlib.hash import md5_crypt
from src.Shared.Exceptions.DecryptForbiddenException import DecryptForbiddenException
from src.Shared.InterfaceAdapters.IEncryption import IEncryption

class Md5EncryptionStrategy(IEncryption):

    def compare(self, chain: str, chainHashed: str) -> bool:
        return md5_crypt.using(salt_size=22).verify(chain, chainHashed)

    def decrypt(self, chain: str):
        raise DecryptForbiddenException()

    def encrypt(self, chain: str) -> str:
        raise DecryptForbiddenException()
