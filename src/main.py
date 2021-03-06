from dotenv import dotenv_values
from fastapi import FastAPI

from src.Shared.Factories.DatabaseFactory import DatabaseFactory
from src.Auth.Presentation.Handlers import AuthHandler
from src.Role.Presentation.Handlers import RoleHandler
from src.User.Presentation.Handlers import UserHandler
from src.Shared.Exceptions.index import handleError

config = dotenv_values(".env")

dbFactory = DatabaseFactory(config, config.get("DB_DEFAULT"))

dbStrategy = dbFactory.create()
dbStrategy.init()
dbStrategy.create()

app = FastAPI()

handleError(app)

app.include_router(AuthHandler.router)
app.include_router(RoleHandler.router)
app.include_router(UserHandler.router)
