
from student.student import Student
from utilities.student_utilites import addDataToJSONFile
import os

current_path = os.getcwd()

print(os.path.join(current_path, 'student'))

class StudentManagementSystem:
    
    def add_student(self, name, age, address, student_id):
        # Create an Instance of Student Class
        student_obj = Student(name, age, address, student_id)
        # Convert Student Object to Dictionary Data 
        student_dict = student_obj.__dict__
        # Save Student Data to a JSON File
        addDataToJSONFile(student_dict, fileName="student_data.json", filePath=os.path.join(current_path, 'student'))
        print(f"Student {student_dict['name']} (ID: {student_dict['student_id']}) added successfully.")
        
    def add_course(self, course_name, course_code, instructor):
        pass
    
    def enroll_in_course(self, studentId, course_code):
        pass
    
    def add_grade(self, studentId, course_code):
        pass
    
    def display_student_details(self):
        pass
    
    def display_course_details(self):
        pass
    
sms = StudentManagementSystem()

def display_menu():
    mainMenu = """
==== Student Management System ====
1. Add New Student
2. Add New Course
3. Enroll Student in Course
4. Add Grade for Student
5. Display Student Details
6. Display Course Details
7. Save Data to File
8. Load Data from File
0. Exit
"""
    print(mainMenu)
    option = input("Select Option: ")
    return option
    
while True:
    
    option = display_menu()
    
    if option == "1":
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        address = input("Enter Address: ")
        student_id = input("Enter Student ID: ")
        sms.add_student(name, age, address, student_id)
    
    elif option == "2":
        pass
    
    elif option == "3":
        pass
    
    elif option == "4":
        pass
    
    elif option == "5":
        pass
    
    elif option == "6":
        pass
    
    elif option == "7":
        pass
    
    elif option == "8":
        pass
    
    elif option == "0":
        exit()
        
    else:
        print("Invalid Option Selected. Please Try Again a Valid Choice.")
    
    