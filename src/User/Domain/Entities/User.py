from dataclasses import dataclass
from typing import List
from pydantic import BaseModel


@dataclass
class User(BaseModel):
    firstName: str
    lastName: str
    email: str
    password: str
    birthday: str
    documentType: str
    documentNumber: int
    gender: str
    phone: str
    country: str
    address: str
    enable: bool
    permissions: List[str]

