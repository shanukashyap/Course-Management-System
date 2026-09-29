from models.user import User


class Student(User):
    """Represents a student in the learning platform."""

    def __init__(self, user_id, name, email, student_level="Beginner"):
        super().__init__(user_id, name, email)
        self.__student_level = student_level
        self.__enrollments = []

    @property
    def student_level(self):
        return self.__student_level

    def enroll(self, enrollment):
        if enrollment not in self.__enrollments:
            self.__enrollments.append(enrollment)

    def get_enrollments(self):
        return self.__enrollments.copy()

    def get_role(self):
        return "Student"

    def display_profile(self):
        print("\n========== STUDENT PROFILE ==========")
        print(f"ID: {self.user_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Level: {self.student_level}")
        print(f"Role: {self.get_role()}")
        print("=" * 38)

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["user_id"],
            data["name"],
            data["email"],
            data.get("student_level", "Beginner")
        )