from models.user import User
from models.student import Student
from models.mentor import Mentor


def main():

    print("========================================")
    print("   USER DOMAIN MODEL DEMONSTRATION")
    print("========================================")

    # Static method demonstration
    print("\n--- STATIC METHOD ---")

    email = "student@example.com"

    print(
        f"Is '{email}' valid?",
        User.validate_email(email)
    )

    # Create Student
    student = Student(
        "S001",
        "Urmil Kashyap",
        "urmil@example.com",
        "Intermediate"
    )

    # Create Mentor
    mentor = Mentor(
        "M001",
        "Rahul Sharma",
        "rahul@example.com",
        "Python and Generative AI"
    )

    # Instance methods
    print("\n--- INSTANCE METHODS ---")

    student.display_profile()
    mentor.display_profile()

    # Polymorphism demonstration
    print("\n--- POLYMORPHISM ---")

    users = [student, mentor]

    for user in users:
        print(
            f"{user.name} -> {user.get_role()}"
        )

    # Class method demonstration
    print("\n--- CLASS METHOD ---")

    print(
        "Total users created:",
        User.get_user_count()
    )

    # Encapsulation demonstration
    print("\n--- ENCAPSULATION ---")

    print("Student ID:", student.user_id)
    print("Student Name:", student.name)
    print("Student Email:", student.email)
    print("Student Level:", student.student_level)


if __name__ == "__main__":
    main()