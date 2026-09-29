from abc import ABC, abstractmethod


class User(ABC):
    """
    Abstract base class for all users.
    Demonstrates abstraction, encapsulation,
    static method, and class method.
    """

    user_count = 0

    def __init__(self, user_id, name, email):
        # Encapsulation using private attributes
        self.__user_id = user_id
        self.__name = name
        self.__email = email

        User.user_count += 1

    # Read-only properties
    @property
    def user_id(self):
        return self.__user_id

    @property
    def name(self):
        return self.__name

    @property
    def email(self):
        return self.__email

    # Static Method
    @staticmethod
    def validate_email(email):
        """
        Validate email format.
        Static method does not require self or cls.
        """
        return "@" in email and "." in email.split("@")[-1]

    # Class Method
    @classmethod
    def get_user_count(cls):
        """
        Return total number of User objects created.
        """
        return cls.user_count

    # Abstract Method
    @abstractmethod
    def get_role(self):
        """
        Child classes must implement this method.
        """
        pass

    # Abstract Method
    @abstractmethod
    def display_profile(self):
        """
        Child classes must implement this method.
        """
        pass

    def __str__(self):
        return f"{self.name} ({self.email})"