from models.user import User


class Mentor(User):
    """Represents a mentor who teaches courses."""

    def __init__(self, user_id, name, email, expertise):
        super().__init__(user_id, name, email)
        self.__expertise = expertise
        self.__courses = []

    @property
    def expertise(self):
        return self.__expertise

    def add_course(self, course):
        if course not in self.__courses:
            self.__courses.append(course)

    def get_courses(self):
        return self.__courses.copy()

    def get_role(self):
        return "Mentor"

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
        return cls(
            data["user_id"],
            data["name"],
            data["email"],
            data["expertise"]
        )