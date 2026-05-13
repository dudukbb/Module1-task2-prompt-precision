from dataclasses import dataclass
from typing import Dict, Optional


@dataclass
class User:
    email: str
    password_hash: str


class UserStore:
    """In-memory user store for demo usage only."""

    def __init__(self) -> None:
        self._users: Dict[str, User] = {}

    def create_user(self, email: str, password_hash: str) -> bool:
        if email in self._users:
            return False

        self._users[email] = User(email=email, password_hash=password_hash)
        return True

    def get_user(self, email: str) -> Optional[User]:
        return self._users.get(email)
