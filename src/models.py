from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime
from bcrypt import hashpw, gensalt


class Peer:
    ip: str
    start_date: datetime = Field(default_factory=datetime.utcnow)
    end_date: datetime
    traffic_used: str
    allowed_traffic: str


class User(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=8)
    phone_number: str = Field(..., min_length=11, max_length=11)
    peers = [Peer]
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    @classmethod
    def hash_password(cls, password: str) -> str:
        return hashpw(password.encode('utf-8'), gensalt()).decode('utf-8')

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return hashpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8')) == hashed_password.encode(
            'utf-8')


