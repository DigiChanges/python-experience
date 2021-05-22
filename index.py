from fastapi import FastAPI
from src.User.Presentation.Handlers import UserHandler


app = FastAPI()

app.include_router(UserHandler.router)
