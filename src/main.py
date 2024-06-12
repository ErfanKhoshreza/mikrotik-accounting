from librouteros import connect
from librouteros.login import plain

# import asyncio
# from models import User
# from database import create_user, get_all_users, update_user_email, delete_user

# async def main():
#     # Insert a few users
#
#
#     # Retrieve all users
#     users = await get_all_users()
#     print("All users:")
#     for user in users:
#         print(user)
#     # Update a user's email
#     updated_count = await update_user_email("alice", "alice_new@example.com")
#     print(f"Updated {updated_count} user's email")
#
#     # Retrieve all users after update
#     users = await get_all_users()
#     print("All users after update:")
#     for user in users:
#         print(user)
#
#     # Delete a user
#     deleted_count = await delete_user("bob")
#     print(f"Deleted {deleted_count} user")
#
#     # Retrieve all users after deletion
#     users = await get_all_users()
#     print("All users after deletion:")
#     for user in users:
#         print(user)
#
# if __name__ == "__main__":
#     asyncio.run(main())

class Main:
    @classmethod
    def connect_to_mikrotik(cls, host, username, password,port):
        session = connect(
            username=username,
            password=password,
            host=host,
            login_method=plain,
            port=port

        )
        return session
test = Main.connect_to_mikrotik("185.24.254.tstt","admin","test",777)

