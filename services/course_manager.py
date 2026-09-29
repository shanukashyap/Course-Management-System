from models.enrollment import Enrollment


class CourseManagementSystem:
    """Main service for managing students, mentors, courses and enrollments."""

    def __init__(self):
        self.__students = {}
        self.__mentors = {}
        self.__courses = {}
        self.__enrollments = []

    def add_student(self, student):
        if student.user_id in self.__students:
            raise ValueError("Student ID already exists.")

        self.__students[student.user_id] = student

    def add_mentor(self, mentor):
        if mentor.user_id in self.__mentors:
            raise ValueError("Mentor ID already exists.")

        self.__mentors[mentor.user_id] = mentor

    def add_course(self, course):
        if course.course_id in self.__courses:
            raise ValueError("Course ID already exists.")

        self.__courses[course.course_id] = course

    def enroll_student(self, student_id, course_id):
        student = self.__students.get(student_id)
        course = self.__courses.get(course_id)

        if not student:
            raise ValueError("Student not found.")

        if not course:
            raise ValueError("Course not found.")

        course.add_student(student)

        enrollment = Enrollment(student, course)
        student.enroll(enrollment)

        self.__enrollments.append(enrollment)

        return enrollment

    def show_students(self):
        print("\n========== STUDENTS ==========")

        for student in self.__students.values():
            print(
                f"{student.user_id} | "
                f"{student.name} | "
                f"{student.email}"
            )

    def show_mentors(self):
        print("\n========== MENTORS ==========")

        for mentor in self.__mentors.values():
            print(
                f"{mentor.user_id} | "
                f"{mentor.name} | "
                f"{mentor.expertise}"
            )

    def show_courses(self):
        print("\n========== COURSES ==========")

        for course in self.__courses.values():
            print(
                f"{course.course_id} | "
                f"{course.title} | "
                f"Mentor: {course.mentor.name} | "
                f"Seats: {course.seats_available()}"
            )

    def show_enrollments(self):
        print("\n========== ENROLLMENTS ==========")

        for enrollment in self.__enrollments:
            print(
                f"{enrollment.student.name} -> "
                f"{enrollment.course.title}"
            )

    def find_student(self, student_id):
        return self.__students.get(student_id)

    def find_course(self, course_id):
        return self.__courses.get(course_id)