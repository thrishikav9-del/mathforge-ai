import json
import uuid
import os
import time
from typing import Dict, Tuple, Optional

BASE_DIR = os.path.dirname(__file__)
USERS_FILE = os.path.join(BASE_DIR, "users.json")
RESET_TOKENS_FILE = os.path.join(BASE_DIR, "reset_tokens.json")

def load_json(file_path, default):
    try:
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                return json.load(f)
    except:
        pass
    return default

def save_json(file_path, data):
    with open(file_path, "w") as f:
        json.dump(data, f, indent=2)

# -------------------- USERS --------------------

def signup_user(username: str, password: str) -> Tuple[bool, str]:
    users_data = load_json(USERS_FILE, {"users": []})

    for user in users_data["users"]:
        if user["username"] == username:
            return False, "Username already exists"

    token = str(uuid.uuid4())

    users_data["users"].append({
        "username": username,
        "password": password,
        "token": token,
        "created_at": time.strftime("%Y-%m-%d %H:%M:%S")
    })

    save_json(USERS_FILE, users_data)
    return True, token

def login_user(username: str, password: str) -> Tuple[bool, str]:
    users_data = load_json(USERS_FILE, {"users": []})

    for user in users_data["users"]:
        if user["username"] == username and user["password"] == password:
            token = str(uuid.uuid4())
            user["token"] = token
            user["last_login"] = time.strftime("%Y-%m-%d %H:%M:%S")
            save_json(USERS_FILE, users_data)
            return True, token

    return False, "Invalid username or password"

def validate_token(token: str) -> bool:
    users_data = load_json(USERS_FILE, {"users": []})
    return any(user.get("token") == token for user in users_data["users"])

def get_user_by_token(token: str) -> Optional[Dict]:
    users_data = load_json(USERS_FILE, {"users": []})
    for user in users_data["users"]:
        if user.get("token") == token:
            return {
                "username": user["username"],
                "created_at": user.get("created_at"),
                "last_login": user.get("last_login")
            }
    return None

# -------------------- PASSWORD CHANGE --------------------

def change_password(username: str, old_password: str, new_password: str) -> Tuple[bool, str]:
    users_data = load_json(USERS_FILE, {"users": []})

    for user in users_data["users"]:
        if user["username"] == username:
            if user["password"] != old_password:
                return False, "Old password incorrect"

            user["password"] = new_password
            user["token"] = str(uuid.uuid4())
            save_json(USERS_FILE, users_data)
            return True, "Password changed successfully"

    return False, "User not found"

# -------------------- RESET FLOW --------------------

def forgot_password(username: str) -> Tuple[bool, str]:
    users_data = load_json(USERS_FILE, {"users": []})

    if not any(user["username"] == username for user in users_data["users"]):
        return False, "Username not found"

    reset_token = str(uuid.uuid4())
    expiry = time.time() + 3600

    tokens_data = load_json(RESET_TOKENS_FILE, {"tokens": []})
    tokens_data["tokens"].append({
        "username": username,
        "reset_token": reset_token,
        "expiry": expiry,
        "used": False
    })

    save_json(RESET_TOKENS_FILE, tokens_data)
    return True, reset_token

def reset_password(reset_token: str, new_password: str) -> Tuple[bool, str]:
    tokens_data = load_json(RESET_TOKENS_FILE, {"tokens": []})
    users_data = load_json(USERS_FILE, {"users": []})

    for token_info in tokens_data["tokens"]:
        if (token_info["reset_token"] == reset_token and
            not token_info["used"] and
            token_info["expiry"] > time.time()):

            token_info["used"] = True

            for user in users_data["users"]:
                if user["username"] == token_info["username"]:
                    user["password"] = new_password
                    user["token"] = str(uuid.uuid4())
                    save_json(USERS_FILE, users_data)
                    save_json(RESET_TOKENS_FILE, tokens_data)
                    return True, "Password reset successfully"

    return False, "Invalid or expired reset token"