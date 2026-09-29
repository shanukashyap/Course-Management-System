# Course Management System

A production-style Python Course Management System demonstrating core Object-Oriented Programming concepts together with a professional Git and GitHub development workflow.

The application manages users, students, mentors, courses, and enrollments while demonstrating abstraction, inheritance, encapsulation, polymorphism, instance methods, static methods, and class methods.

---

## Problem Statement

Educational platforms need a structured way to manage students, mentors, courses, and enrollments.

The objective of this project is to build a maintainable Course Management System using Python OOP principles.

The system should be able to:

* Represent different types of users
* Manage students and mentors
* Create and manage courses
* Associate mentors with courses
* Enroll students into courses
* Track available course capacity
* Demonstrate different OOP principles
* Maintain a clean and scalable project structure
* Demonstrate professional Git/GitHub collaboration

---

## Features

### User Management

* Abstract `User` base class
* Student and Mentor subclasses
* Encapsulated user information
* Email validation
* User count tracking

### Student Management

* Student profile
* Student learning level
* Course enrollment tracking

### Mentor Management

* Mentor profile
* Mentor expertise
* Course assignment

### Course Management

* Course creation
* Mentor assignment
* Course capacity
* Available seat calculation
* Student management

### Enrollment Management

* Student-course relationship
* Enrollment timestamp
* Duplicate enrollment prevention
* Capacity validation

### OOP Demonstrations

* Abstraction
* Inheritance
* Encapsulation
* Polymorphism
* Instance methods
* Static methods
* Class methods

---

## Architecture

```text
Course-Management-System/
│
├── main.py
│
├── models/
│   ├── __init__.py
│   ├── user.py
│   ├── student.py
│   ├── mentor.py
│   ├── course.py
│   └── enrollment.py
│
├── services/
│   ├── __init__.py
│   └── course_manager.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Class Architecture

```text
                    User (ABC)
                    /        \
                   /          \
              Student         Mentor
                 │               │
                 └───────┬───────┘
                         │
                       Course
                         │
                    Enrollment
                         │
                  CourseManager
```

---

## Classes

### User

`User` is the abstract base class.

Responsibilities:

* Store common user information
* Validate email addresses
* Track user count
* Define abstract user behavior

Important methods:

```python
get_role()
display_profile()
validate_email()
get_user_count()
```

---

### Student

`Student` inherits from `User`.

Responsibilities:

* Store student level
* Manage student enrollments
* Display student profile

Inheritance:

```python
class Student(User):
```

---

### Mentor

`Mentor` inherits from `User`.

Responsibilities:

* Store expertise
* Manage assigned courses
* Display mentor profile

Inheritance:

```python
class Mentor(User):
```

---

### Course

The `Course` class represents a learning course.

Responsibilities:

* Store course information
* Assign a mentor
* Manage capacity
* Add and remove students
* Calculate available seats

---

### Enrollment

`Enrollment` connects a student with a course.

It stores:

* Student
* Course
* Enrollment timestamp

---

### CourseManagementSystem

This service class coordinates the application.

Responsibilities:

* Add students
* Add mentors
* Add courses
* Enroll students
* Search for students
* Search for courses
* Display system information

---

# OOP Concepts Demonstrated

## 1. Abstraction

The `User` class is abstract:

```python
from abc import ABC, abstractmethod


class User(ABC):

    @abstractmethod
    def get_role(self):
        pass
```

The abstract class defines behavior that subclasses must implement.

---

## 2. Inheritance

`Student` and `Mentor` inherit from `User`:

```python
class Student(User):
```

```python
class Mentor(User):
```

This allows common user behavior to be reused.

---

## 3. Encapsulation

Sensitive/internal attributes use double underscores:

```python
self.__email
self.__name
self.__user_id
```

Access is provided through properties:

```python
@property
def email(self):
    return self.__email
```

This protects internal object state.

---

## 4. Polymorphism

Both `Student` and `Mentor` implement:

```python
get_role()
```

with different results.

Example:

```python
users = [student, mentor]

for user in users:
    print(user.get_role())
```

Output:

```text
Student
Mentor
```

The same method call behaves differently depending on the object.

---

## 5. Instance Methods

Instance methods operate on individual objects.

Example:

```python
student.display_profile()
```

and:

```python
course.add_student(student)
```

---

## 6. Static Method

Email validation does not require a specific object instance:

```python
@staticmethod
def validate_email(email):
    return "@" in email and "." in email.split("@")[-1]
```

Usage:

```python
User.validate_email("student@example.com")
```

---

## 7. Class Method

The class method works with class-level data:

```python
@classmethod
def get_user_count(cls):
    return User.user_count
```

Usage:

```python
User.get_user_count()
```

---

# Installation

## Requirements

* Python 3.10+
* Git
* GitHub account
* Visual Studio Code or another Python IDE

No external Python packages are required.

---

## Clone the Repository

```bash
git clone https://github.com/shanukashyap/Course-Management-System.git
```

Enter the project:

```bash
cd Course-Management-System
```

---

## Optional Virtual Environment

Create a virtual environment:

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

---

## Run the Application

```bash
python main.py
```

---

# Usage Example

The application creates a student:

```python
student = Student(
    "S001",
    "Urmil Kashyap",
    "urmil@example.com",
    "Intermediate"
)
```

A mentor:

```python
mentor = Mentor(
    "M001",
    "Rahul Sharma",
    "rahul@example.com",
    "Python and Generative AI"
)
```

A course:

```python
course = Course(
    "C001",
    "Python and Generative AI",
    mentor,
    capacity=30
)
```

The student can then be enrolled:

```python
enrollment = system.enroll_student(
    "S001",
    "C001"
)
```

---

# Example Output

```text
========== STATIC METHOD ==========
Valid email: True

========== STUDENT PROFILE ==========
ID: S001
Name: Urmil Kashyap
Email: urmil@example.com
Level: Intermediate
Role: Student
======================================

========== MENTOR PROFILE ==========
ID: M001
Name: Rahul Sharma
Email: rahul@example.com
Expertise: Python and Generative AI
Role: Mentor
====================================

========== COURSE ==========
Course ID: C001
Title: Python and Generative AI
Mentor: Rahul Sharma
Capacity: 30
Seats Available: 29
============================

========== ENROLLMENT ==========
Student: Urmil Kashyap
Course: Python and Generative AI
Mentor: Rahul Sharma
================================

========== POLYMORPHISM DEMO ==========
Urmil Kashyap: Student
Rahul Sharma: Mentor
========================================

========== CLASS METHOD ==========
Total users created: 2
```

---

# Git/GitHub Workflow

The project was developed using feature branches.

## Main Branch

The `main` branch contains the stable production version.

## Feature Branches

### `feature-user-model`

Responsible for:

* User
* Student
* Mentor
* Abstraction
* Inheritance
* Encapsulation

### `feature-course-enrollment`

Responsible for:

* Course
* Enrollment
* Capacity management
* Enrollment validation

### `feature-course-manager`

Responsible for:

* CourseManagementSystem
* Application integration
* CLI demonstration

---

## Example Git Workflow

Create a feature branch:

```bash
git switch -c feature-user-model
```

Develop the feature.

Commit:

```bash
git add .
git commit -m "Add user hierarchy with student and mentor models"
```

Push:

```bash
git push -u origin feature-user-model
```

Create a Pull Request on GitHub.

After review, merge the Pull Request into `main`.

---

# Pull Requests

The project uses GitHub Pull Requests to simulate a team development workflow.

Pull Requests provide an opportunity to:

* Review code
* Discuss changes
* Check implementation
* Keep `main` stable
* Merge completed features

---

# Testing

Run the application:

```bash
python main.py
```

Verify:

* Student creation
* Mentor creation
* Course creation
* Student enrollment
* Profile display
* Course display
* Enrollment display
* Email validation
* Polymorphism
* Class-level user count

---

# Git History

View the project history:

```bash
git log --oneline --graph --decorate --all
```

Check branches:

```bash
git branch -a
```

Check repository status:

```bash
git status
```

---

# Future Improvements

Possible future enhancements include:

* SQLite/PostgreSQL database
* REST API using FastAPI
* Authentication and authorization
* Course search
* Course completion tracking
* Payment integration
* Admin dashboard
* Unit tests with pytest
* Docker deployment
* CI/CD with GitHub Actions
* Web frontend using React

---

# Repository

GitHub:

https://github.com/shanukashyap/Course-Management-System

---

# Video Demonstration link

https://youtu.be/jFfRSUBTG0M



1. Problem statement
2. Project architecture
3. Class relationships
4. Abstraction
5. Inheritance
6. Encapsulation
7. Polymorphism
8. Instance methods
9. Static methods
10. Class methods
11. Course enrollment
12. Git branching
13. Commits
14. Pull Requests
15. Merging
16. Application execution
17. Final output
18. GitHub repository

---

# Learning Outcome

This project demonstrates how Python OOP principles can be combined with a professional Git/GitHub development workflow to build a maintainable Course Management System.

The project separates responsibilities across models and services while using feature branches and Pull Requests to simulate collaborative software development.
