from datetime import datetime


class Enrollment:
    """Connects a Student with a Course."""

    enrollment_count = 0

    def __init__(self, student, course):
        self.__student = student
        self.__course = course
        self.__enrolled_at = datetime.now()

        Enrollment.enrollment_count += 1

    @property
    def student(self):
        return self.__student

    @property
    def course(self):
        return self.__course

    @property
    def enrolled_at(self):
        return self.__enrolled_at

    def display_enrollment(self):
        print("\n========== ENROLLMENT ==========")
        print(f"Student: {self.student.name}")
        print(f"Course: {self.course.title}")
        print(f"Mentor: {self.course.mentor.name}")
        print(
            f"Enrolled At: "
            f"{self.enrolled_at.strftime('%Y-%m-%d %H:%M:%S')}"
        )
        print("=" * 32)

    def __str__(self):
        return f"{self.student.name} -> {self.course.title}"