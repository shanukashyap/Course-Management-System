from abc import ABC, abstractmethod


class User(ABC):
    """Abstract base class for all users."""

    user_count = 0

    def __init__(self, user_id, name, email):
        self.__user_id = user_id
        self.__name = name
        self.__email = email

        User.user_count += 1

    @property
    def user_id(self):
        return self.__user_id

    @property
    def name(self):
        return self.__name

    @property
    def email(self):
        return self.__email

    @staticmethod
    def validate_email(email):
        """Validate whether an email has a basic valid format."""
        return "@" in email and "." in email.split("@")[-1]

    @classmethod
    def get_user_count(cls):
        """Return the number of User objects created."""
        return User.user_count

    @abstractmethod
    def get_role(self):
        """Return the role of the user."""
        pass

    @abstractmethod
    def display_profile(self):
        """Display user profile."""
        pass

    def __str__(self):
        return f"{self.__name} ({self.__email})"