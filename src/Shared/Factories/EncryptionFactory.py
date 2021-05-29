from src.Shared.Encryptions.BcryptEncryptionStrategy import BcryptEncryptionStrategy
from src.Shared.Encryptions.Md5EncryptionStrategy import Md5EncryptionStrategy
from src.Shared.InterfaceAdapters.IEncryption import IEncryption


class EncryptionFactory():

    @staticmethod
    def create(encryptionConfig: str = "bcrypt") -> IEncryption:

        encryptions = {
            "bcrypt" : BcryptEncryptionStrategy(),
            "md5" : Md5EncryptionStrategy()
        }

        return encryptions[encryptionConfig]
