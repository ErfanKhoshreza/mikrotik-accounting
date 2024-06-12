import motor.motor_asyncio
from models import User
from pydantic import BaseModel
from typing import List, Type
from datetime import datetime

# Connect to MongoDB
client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')
db = client['mydatabase']


# Insert a new user
async def create_user(user: User) -> None:
    user.password = User.hash_password(user.password)
    document = user.dict(by_alias=True)
    document["created_at"] = document["created_at"].isoformat()
    document["updated_at"] = document["updated_at"].isoformat()
    await db['users'].insert_one(document)


# Retrieve all users
async def get_all_users() -> List[User]:
    users_cursor = db['users'].find()
    users = await users_cursor.to_list(length=100)
    return [User(**user) for user in users]


# Delete a user
async def delete_user(username: str) -> int:
    try:
         result = await db['users'].delete_one({'username': username})
    except Exception as e:
        print(f"Error in Deleting Account With Error {e}")
    return result.deleted_count


async def find_user(username: str, plain_password) -> User:
    try:
        user: User = await db['users'].find_one({'username': username, 'password': User.hash_password(plain_password)})
        if user:
            return user
        else:
            raise ValueError("Username Or Password Is Wrong")
    except Exception as e:
        print(f"Error In Finding User {e}")
