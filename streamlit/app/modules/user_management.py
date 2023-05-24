import pandas as pd
from typing import Optional
from data_management import load_data, save_data, add_row_to_data, update_row_in_data, delete_row_from_data

class User:
    def __init__(self, id: int, username: str, password: str, email: str):
        self.id = id
        self.username = username
        self.password = password
        self.email = email

def create_user(username: str, password: str, email: str) -> User:
    users_data = load_data("users.csv")
    new_user_data = {"username": username, "password": password, "email": email}
    updated_users_data = add_row_to_data(users_data, new_user_data)
    save_data(updated_users_data, "users.csv")
    new_user_id = updated_users_data.index[-1]
    return User(new_user_id, username, password, email)

def authenticate_user(username: str, password: str) -> bool:
    user = get_user_by_username(username)
    if user and user.password == password:
        return True
    return False

def authorize_user(user: User) -> bool:
    # Dummy implementation, as Auth0 is used for authorization
    return True

def get_user_by_username(username: str) -> Optional[User]:
    users_data = load_data("users.csv")
    user_row = users_data.loc[users_data["username"] == username]
    if not user_row.empty:
        user_id = user_row.index[0]
        return User(user_id, username, user_row["password"].iloc[0], user_row["email"].iloc[0])
    return None

def get_user_by_id(user_id: int) -> Optional[User]:
    users_data = load_data("users.csv")
    user_row = users_data.loc[user_id]
    if not user_row.empty:
        return User(user_id, user_row["username"], user_row["password"], user_row["email"])
    return None

def update_user(user: User, new_data: dict) -> User:
    users_data = load_data("users.csv")
    updated_users_data = update_row_in_data(users_data, user.id, new_data)
    save_data(updated_users_data, "users.csv")
    updated_user = get_user_by_id(user.id)
    return updated_user

def delete_user(user: User) -> bool:
    users_data = load_data("users.csv")
    updated_users_data = delete_row_from_data(users_data, user.id)
    save_data(updated_users_data, "users.csv")
    return True