from models.user import User


class Mentor(User):
    """
    Mentor inherits from User.
    Demonstrates inheritance and polymorphism.
    """

    def __init__(self, user_id, name, email, expertise):
        super().__init__(user_id, name, email)

        self.__expertise = expertise
        self.__courses = []

    @property
    def expertise(self):
        return self.__expertise

    def add_course(self, course):
        """Add a course taught by the mentor."""
        if course not in self.__courses:
            self.__courses.append(course)

    def get_courses(self):
        """Return a copy of mentor's courses."""
        return self.__courses.copy()

    # Implement abstract method
    def get_role(self):
        return "Mentor"

    # Implement abstract method
    def display_profile(self):
        print("\n========== MENTOR PROFILE ==========")
        print(f"ID: {self.user_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Expertise: {self.expertise}")
        print(f"Role: {self.get_role()}")
        print("=" * 36)

    @classmethod
    def from_dict(cls, data):
        """
        Alternative constructor using class method.
        """
        return cls(
            data["user_id"],
            data["name"],
            data["email"],
            data["expertise"]
        )