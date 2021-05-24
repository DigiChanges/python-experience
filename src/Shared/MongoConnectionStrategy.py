from index import config
from mongoengine import connect, Document

host=config.get("DB_HOST")
user=config.get("DB_HOST")
password=config.get("DB_HOST")
database=config.get("DB_HOST")
port=config.get("DB_HOST")

connect(host=f"mongodb://{user}:{password}@{host}:{port}/{database}?authSource={database}")

class User(Document):
    pass
