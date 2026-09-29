class Course:
    """Represents a course offered by a mentor."""

    course_count = 0

    def __init__(self, course_id, title, mentor, capacity=30):
        self.__course_id = course_id
        self.__title = title
        self.__mentor = mentor
        self.__capacity = capacity
        self.__students = []

        Course.course_count += 1

        mentor.add_course(self)

    @property
    def course_id(self):
        return self.__course_id

    @property
    def title(self):
        return self.__title

    @property
    def mentor(self):
        return self.__mentor

    @property
    def capacity(self):
        return self.__capacity

    def add_student(self, student):
        if student in self.__students:
            raise ValueError("Student is already enrolled.")

        if len(self.__students) >= self.__capacity:
            raise ValueError("Course capacity has been reached.")

        self.__students.append(student)

    def remove_student(self, student):
        if student in self.__students:
            self.__students.remove(student)

    def get_students(self):
        return self.__students.copy()

    def seats_available(self):
        return self.__capacity - len(self.__students)

    def display_course(self):
        print("\n========== COURSE ==========")
        print(f"Course ID: {self.course_id}")
        print(f"Title: {self.title}")
        print(f"Mentor: {self.mentor.name}")
        print(f"Capacity: {self.capacity}")
        print(f"Seats Available: {self.seats_available()}")
        print("=" * 28)

    @classmethod
    def from_dict(cls, data, mentor):
        return cls(
            data["course_id"],
            data["title"],
            mentor,
            data.get("capacity", 30)
        )

    def __str__(self):
        return f"{self.course_id} - {self.title}"