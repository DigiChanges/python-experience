from mongoengine import connect, disconnect
from src.Shared.InterfaceAdapters.ICreateConnection import ICreateConnection

class MongoCreateConnectionStrategy(ICreateConnection):
    host: str
    user: str
    password: str
    database: str
    port: int
    uri: str

    def __init__(self, config):
        self.host=config.get("DB_HOST")
        self.user=config.get("DB_USER")
        self.password=config.get("DB_PASSWORD")
        self.database=config.get("DB_DATABASE")
        self.port=config.get("DB_PORT")

    def init(self):
        self.uri = f"mongodb://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}?authSource={self.database}"

    def create(self):
        return connect(host=self.uri)

    def close(self):
        disconnect()
