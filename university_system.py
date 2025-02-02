# university_system.py

class Student:
    def __init__(self, student_id, name, age, gender, courses=None):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.gender = gender
        self.courses = courses if courses else []
        self.grades = {}

    def register_course(self, course_name):
        """Register a course for the student."""
        if course_name not in self.courses:
            self.courses.append(course_name)
            print(f"{self.name} has been registered for the course: {course_name}")
        else:
            print(f"{self.name} is already registered for the course: {course_name}")

    def assign_grade(self, course_name, grade):
        """Assign a grade to a student in a specific course."""
        if course_name in self.courses:
            self.grades[course_name] = grade
            print(f"{self.name}'s grade for {course_name} has been assigned: {grade}")
        else:
            print(f"{self.name} is not registered for the course: {course_name}")

    def get_grade(self, course_name):
        """Get the grade for a student in a specific course."""
        return self.grades.get(course_name, "No grade assigned")

    def __repr__(self):
        return f"Student({self.student_id}, {self.name}, {self.age}, {self.gender}, Courses: {self.courses}, Grades: {self.grades})"


class UniversitySystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name, age, gender):
        """Add a new student to the system."""
        if student_id not in self.students:
            student = Student(student_id, name, age, gender)
            self.students[student_id] = student
            print(f"Student {name} added successfully.")
        else:
            print(f"Student ID {student_id} already exists.")

    def register_student_course(self, student_id, course_name):
        """Register a student for a course."""
        student = self.students.get(student_id)
        if student:
            student.register_course(course_name)
        else:
            print(f"Student ID {student_id} not found.")

    def assign_student_grade(self, student_id, course_name, grade):
        """Assign a grade to a student."""
        student = self.students.get(student_id)
        if student:
            student.assign_grade(course_name, grade)
        else:
            print(f"Student ID {student_id} not found.")

    def get_student_grade(self, student_id, course_name):
        """Get the grade of a student in a specific course."""
        student = self.students.get(student_id)
        if student:
            grade = student.get_grade(course_name)
            print(f"{student.name}'s grade for {course_name}: {grade}")
        else:
            print(f"Student ID {student_id} not found.")

    def display_all_students(self):
        """Display all students and their details."""
        if not self.students:
            print("No students found.")
        else:
            for student in self.students.values():
                print(student)


def main():
    university_system = UniversitySystem()

    while True:
        print("\nUniversity Admission & Maintenance System")
        print("1. Add Student")
        print("2. Register Student for Course")
        print("3. Assign Grade to Student")
        print("4. Get Student Grade")
        print("5. View All Students")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            student_id = input("Enter student ID: ").strip()
            name = input("Enter student name: ").strip()
            age = int(input("Enter student age: ").strip())
            gender = input("Enter student gender (Male/Female): ").strip()
            university_system.add_student(student_id, name, age, gender)

        elif choice == '2':
            student_id = input("Enter student ID: ").strip()
            course_name = input("Enter course name: ").strip()
            university_system.register_student_course(student_id, course_name)

        elif choice == '3':
            student_id = input("Enter student ID: ").strip()
            course_name = input("Enter course name: ").strip()
            grade = input("Enter grade: ").strip()
            university_system.assign_student_grade(student_id, course_name, grade)

        elif choice == '4':
            student_id = input("Enter student ID: ").strip()
            course_name = input("Enter course name: ").strip()
            university_system.get_student_grade(student_id, course_name)

        elif choice == '5':
            university_system.display_all_students()

        elif choice == '6':
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
