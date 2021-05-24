from dotenv import dotenv_values
from fastapi import FastAPI

from src.Shared.Exceptions.index import handleError

from src.User.Presentation.Handlers import UserHandler

config = dotenv_values(".env")

app = FastAPI()

handleError(app)

app.include_router(UserHandler.router)
