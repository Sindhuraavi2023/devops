import sys

# Define a class to represent a Student
class Student:
    """A class to represent a student in the management system."""
    def __init__(self, name, roll_number, age):
        self.name = name
        self.roll_number = roll_number
        self.age = age
        self.grades = {}  # A dictionary to store grades by subject

    def __str__(self):
        """String representation of the Student object."""
        return (f"Name: {self.name}\n"
                f"Roll Number: {self.roll_number}\n"
                f"Age: {self.age}")

    def add_grade(self, subject, grade):
        """Adds a grade for a specific subject."""
        self.grades[subject] = grade

    def get_average_grade(self):
        """Calculates the average grade for the student."""
        if not self.grades:
            return 0.0
        return sum(self.grades.values()) / len(self.grades)

# Define a class to manage all student operations
class StudentManager:
    """Manages a collection of students."""
    def __init__(self):
        self.students = []

    def add_student(self, name, roll_number, age):
        """Adds a new student to the system."""
        # Check if a student with the same roll number already exists
        if any(s.roll_number == roll_number for s in self.students):
            print(f"Error: A student with roll number {roll_number} already exists.")
            return False
        
        try:
            student = Student(name, roll_number, age)
            self.students.append(student)
            print(f"Successfully added student: {name} (Roll No. {roll_number})")
            return True
        except ValueError as e:
            print(f"Error adding student: {e}")
            return False

    def view_all_students(self):
        """Displays details of all students in the system."""
        if not self.students:
            print("No students in the system.")
            return

        print("\n--- All Students ---")
        for i, student in enumerate(self.students, 1):
            print(f"\n--- Student {i} ---")
            print(student)
            if student.grades:
                print("Grades:")
                for subject, grade in student.grades.items():
                    print(f"  - {subject}: {grade}")
                print(f"  Average Grade: {student.get_average_grade():.2f}")
            else:
                print("Grades: Not yet available")
        print("--------------------\n")

    def find_student(self, roll_number):
        """Finds and returns a student by their roll number."""
        for student in self.students:
            if student.roll_number == roll_number:
                return student
        return None

    def update_student_grades(self, roll_number, subject, grade):
        """Updates the grade for a specific student and subject."""
        student = self.find_student(roll_number)
        if not student:
            print(f"Error: Student with roll number {roll_number} not found.")
            return False
        
        try:
            student.add_grade(subject, float(grade))
            print(f"Successfully updated grade for {student.name} in {subject}.")
            return True
        except ValueError:
            print("Error: Invalid grade. Please enter a number.")
            return False

    def delete_student(self, roll_number):
        """Deletes a student from the system by their roll number."""
        student_to_delete = self.find_student(roll_number)
        if not student_to_delete:
            print(f"Error: Student with roll number {roll_number} not found.")
            return False
        
        self.students.remove(student_to_delete)
        print(f"Successfully deleted student: {student_to_delete.name}.")
        return True

# Main function to run the student management application
def main():
    manager = StudentManager()

    while True:
        print("\n--- Student Management System Menu ---")
        print("1. Add a new student")
        print("2. View all students")
        print("3. Update student grades")
        print("4. Delete a student")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter student's name: ")
            roll_number = input("Enter student's roll number: ")
            age = input("Enter student's age: ")
            
            try:
                manager.add_student(name, roll_number, int(age))
            except ValueError:
                print("Error: Age must be a number.")
        
        elif choice == '2':
            manager.view_all_students()

        elif choice == '3':
            roll_number = input("Enter the student's roll number to update grades: ")
            student = manager.find_student(roll_number)
            if student:
                subject = input(f"Enter the subject for {student.name}'s grade: ")
                grade = input(f"Enter the grade for {subject}: ")
                manager.update_student_grades(roll_number, subject, grade)
        
        elif choice == '4':
            roll_number = input("Enter the student's roll number to delete: ")
            manager.delete_student(roll_number)

        elif choice == '5':
            print("Exiting Student Management System. Goodbye!")
            sys.exit(0)

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
