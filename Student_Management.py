class Student:
    """Class to represent a Student"""
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

class StudentManagementSystem:
    """Class to manage student records"""
    def __init__(self):
        self.students = []

    def add_student(self, roll_no, name, marks):
        student = Student(roll_no, name, marks)
        self.students.append(student)
        print(f"Student {name} added successfully!")

    def view_students(self):
        if not self.students:
            print("No student records found.")
        else:
            print("\n--- Student Records ---")
            for student in self.students:
                print(f"Roll No: {student.roll_no}, Name: {student.name}, Marks: {student.marks}")
            print("------------------------")

    def search_student(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                print(f"Student Found: Roll No: {student.roll_no}, Name: {student.name}, Marks: {student.marks}")
                return
        print("Student not found.")

    def delete_student(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                self.students.remove(student)
                print(f"Student with Roll No {roll_no} deleted successfully!")
                return
        print("Student not found.")

def main():
    system = StudentManagementSystem()

    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            roll_no = input("Enter Roll No: ")
            name = input("Enter Name: ")
            marks = input("Enter Marks: ")
            system.add_student(roll_no, name, marks)
        elif choice == '2':
            system.view_students()
        elif choice == '3':
            roll_no = input("Enter Roll No to search: ")
            system.search_student(roll_no)
        elif choice == '4':
            roll_no = input("Enter Roll No to delete: ")
            system.delete_student(roll_no)
        elif choice == '5':
            print("Exiting the Student Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
