from models.student import Student
from models.mentor import Mentor
from models.course import Course
from services.course_manager import CourseManagementSystem


def demonstrate_polymorphism(users):
    print("\n========== POLYMORPHISM DEMO ==========")

    for user in users:
        print(f"{user.name}: {user.get_role()}")

    print("=" * 40)


def main():
    system = CourseManagementSystem()

    # Create users
    student = Student(
        "S001",
        "Urmil Kashyap",
        "urmil@example.com",
        "Intermediate"
    )

    mentor = Mentor(
        "M001",
        "Rahul Sharma",
        "rahul@example.com",
        "Python and Generative AI"
    )

    # Create course
    course = Course(
        "C001",
        "Python and Generative AI",
        mentor,
        capacity=30
    )

    # Register users and course
    system.add_student(student)
    system.add_mentor(mentor)
    system.add_course(course)

    # Static method demonstration
    print("\n========== STATIC METHOD ==========")

    print(
        "Valid email:",
        UserEmailDemo.validate_email("student@example.com")
    )

    # Enrollment
    enrollment = system.enroll_student("S001", "C001")

    # Display information
    student.display_profile()
    mentor.display_profile()
    course.display_course()
    enrollment.display_enrollment()

    system.show_students()
    system.show_mentors()
    system.show_courses()
    system.show_enrollments()

    # Polymorphism
    demonstrate_polymorphism([student, mentor])

    # Class method
    print("\n========== CLASS METHOD ==========")
    print(
        "Total users created:",
        Student.get_user_count()
    )


class UserEmailDemo:
    """Small helper for demonstrating a static method."""

    @staticmethod
    def validate_email(email):
        return "@" in email and "." in email.split("@")[-1]


if __name__ == "__main__":
    main()