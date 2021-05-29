# import Config from 'config';
# import bcrypt from 'bcrypt';
# import {IEncryption} from '@digichanges/shared-experience';
from src.Shared.Exceptions.DecryptForbiddenException import DecryptForbiddenException
from src.Shared.Config import config

from src.Shared.InterfaceAdapters.IEncryption import IEncryption


class BcryptEncryptionStrategy(IEncryption):

    def compare(chain: str, chainHashed: str) -> bool:
        return bcrypt.compare(chain, chainHashed)

    def decrypt(chain: str) -> str:
        raise DecryptForbiddenException()

    def encrypt(chain: str) -> str:
        saltRounds: int = config.get('encryption', {}).get('bcrypt', {}).get('saltRounds', 10);

        return bcrypt.hash(chain, saltRounds)

