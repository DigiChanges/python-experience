from dotenv import dotenv_values
from fastapi import FastAPI
from src.User.Presentation.Handlers import UserHandler

config = dotenv_values(".env")

app = FastAPI()

app.include_router(UserHandler.router)
