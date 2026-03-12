import re
from typing import Optional


class User:
    """Create a user with a first name, last name, and email address\n
    Emeil field with validation
    """
    def __init__(self, first_name: str, last_name: str, email: str) -> None:
        """Initialize a new User instance"""
        self._first_name = first_name
        self._last_name = last_name
        self._email = None
        self.email = email

    @property
    def first_name(self) -> str:
        """Get the user's first name"""
        return self._first_name

    @first_name.setter
    def first_name(self, value: str) -> None:
        """Set the user's first name"""
        if not value:
            raise ValueError("First name cant be empty")
        self._first_name = value

    @property
    def last_name(self) -> str:
        """Get the user's last name"""
        return self._last_name

    @last_name.setter
    def last_name(self, value: str) -> None:
        """Set the user's last name"""
        if not value:
            raise ValueError("Last name cant be empty")
        self._last_name = value

    @property
    def email(self) -> Optional[str]:
        """Get the user's email address"""
        return self._email

    @email.setter
    def email(self, value: str) -> None:
        """Set the user's email address"""
        if not self.is_valid_email(value):
            raise ValueError("Invalid email format")
        self._email = value

    @staticmethod
    def is_valid_email(email) -> bool:
        """Validate the email address format"""
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return re.match(pattern, email) is not None


if __name__ == "__main__":
    user = None
    try:
        user = User("Lesia", "Ladan", "ladan.l@example.com")
        print(user.first_name, user.last_name, user.email)
    except ValueError as err:
        print(err)

    if user is not None:
        print("Current user:", user.first_name, user.last_name, user.email)

    try:
        user = User("Lesia", "Ladan", "ladan.lexample.com")
        print(user.first_name, user.last_name, user.email)
    except ValueError as err:
        print(err)

    try:
        user = User("Lesia", "Ladan", "ladan.l@example.com")
        print(user.first_name, user.last_name, user.email)
        user.first_name = ""
    except ValueError as err:
        print("Error:", err)

    try:
        user = User("Lesia", "Ladan", "ladan.l@example.com")
        print(user.first_name, user.last_name, user.email)
        user.last_name = ""
    except ValueError as err:
        print("Error:", err)

    try:
        user = User("Lesia", "Ladan", "ladan.l@example.com")
        print(user.first_name, user.last_name, user.email)
        user.first_name = "Lesya"
    except ValueError as err:
        print("Error:", err)
