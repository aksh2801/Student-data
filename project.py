class Student:
    def __init__(self,roll_number,name,class_name):
        self.roll_number = roll_number
        self.name = name
        self.class_name = class_name
        self.marks = {}

    def add_marks(self,subject,marks):
        if subject in self.marks:
            print(f"Already has marks for {subject}")
        else:
            self.marks[subject] = marks

    def calculate_average_marks(self):
        if not self.marks:
            print("there are no available marks")
        total_marks = sum(self.marks.values())
        average_marks = total_marks/len(self.marks)
        return average_marks

    def display_student_info(self):
        print(f"student information")
        print(f"roll number : {self.roll_number}")
        print(f"name : {self.name}")
        print(f"class : {self.class_name}")
        print(f"marks : {self.marks}")
        print(f"average marks are : {self.calculate_average_marks()}")

def create_student():
    roll_number = int(input("Enter roll number: "))
    name = input("Enter student's name: ")
    class_name = input("Enter class name: ")
    student = Student(roll_number, name, class_name)

    while True:
        subject = input("Enter subject name (or type 'done' to finish): ")
        if subject.lower() == 'done':
            break
        marks = float(input(f"Enter marks for {subject}: "))
        student.add_marks(subject, marks)
    return student

students = []
while True:
    students.append(create_student())  # Add each student to the list
    another = input("Do you want to enter another student? (yes/no): ").lower()
    if another != 'yes':  
        break

for student in students:
    student.display_student_info()