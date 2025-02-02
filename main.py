# main.py

from university_system import UniversitySystem

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
