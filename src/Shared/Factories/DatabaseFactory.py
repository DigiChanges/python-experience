from typing import Any

from src.Shared.Database.MongoConnectionStrategy import MongoCreateConnectionStrategy
from src.Shared.InterfaceAdapters.ICreateConnection import ICreateConnection


class DatabaseFactory:
    __dbDefault: str
    __config: Any

    def __init__(self, config, dbDefault: str = "Mongo"):
        self.__dbDefault = dbDefault
        self.__config = config

    def create(self) -> ICreateConnection:
        createConnection = None

        if self.__dbDefault == 'Mongo':
            createConnection = MongoCreateConnectionStrategy(self.__config)

        return createConnection
