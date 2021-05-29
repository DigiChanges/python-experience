from passlib.hash import pbkdf2_sha512
from src.Shared.Exceptions.DecryptForbiddenException import DecryptForbiddenException
from src.Shared.InterfaceAdapters.IEncryption import IEncryption

class BcryptEncryptionStrategy(IEncryption):

    def compare(self, chain: str, chainHashed: str) -> bool:
        return pbkdf2_sha512.using(salt_size=22).verify(chain, chainHashed)

    def decrypt(self, chain: str):
        raise DecryptForbiddenException()

    def encrypt(self, chain: str) -> str:
        return pbkdf2_sha512.using(salt_size=22).encrypt(chain)
