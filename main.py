
from student.student import Student
from course.course import Course
from utilities.student_utilites import addDataToJSONFile
from utilities.student_utilites import loadDataFromJSONFile
import os

current_path = os.getcwd()

class StudentManagementSystem:
    
    def __init__(self):
        # Load students data from student_data.json file
        students = loadDataFromJSONFile(fileName="student_data.json", filePath=os.path.join(current_path, 'student'))
        # Load courses data from course_data.json file
        courses = loadDataFromJSONFile(fileName="course_data.json", filePath=os.path.join(current_path, 'course'))
        
        # Convert the list of student dictionaries into Student objects
        self.students = StudentManagementSystem.dictToObject(list=students, class_name=Student)
        # Convert the list of course dictionaries into Course objects
        self.courses = StudentManagementSystem.dictToObject(list=courses, class_name=Course)
        
        # Enroll each student in their respective courses by matching course codes and adding them to the course's student list
        for student in self.students:
            if hasattr(student, 'courses'):
                for enrolled_course in student.courses:
                    for course in self.courses:
                        if course.course_code == enrolled_course["course_code"]:
                            course.add_student(student)
                            break
                
    def add_student(self, name, age, address, student_id):
        existing_student = StudentManagementSystem.record_exists(records=self.students, searchKey="student_id", searchValue=student_id)
        if existing_student:
             # Print an error message advising the user that the student id already exists
            print(f"Student with ID {student_id} already exists. Please enter a unique student ID.")
            return
        # Create an Instance of Student Class
        student_obj = Student(name, age, address, student_id)
        # Convert Student Object to Distonary Data
        student_dict = student_obj.__dict__
        # Save Student Data to a JSON File
        response = addDataToJSONFile(student_dict, fileName="student_data.json", filePath=os.path.join(current_path, 'student'))
        # Check if the response indicates a successful course creation
        if response['acknowledged']:
            self.students.append(student_obj)
            print(f"Student {student_obj.name} (ID: {student_obj.student_id}) added successfully.")
        
        
    def add_course(self, course_name, course_code, instructor):
        existing_course = StudentManagementSystem.record_exists(records=self.courses, searchKey="course_code", searchValue=course_code)
        
        if existing_course:
            print(f"Course with code {course_code} already exists. Please enter a unique course code.")
            return
        # Create an Instance of Course Class
        course_obj = Course(course_name, course_code, instructor)
        # Convert Course Object to Distonary Data
        course_dict = course_obj.__dict__
        # Save Course Data to a JSON File
        response = addDataToJSONFile(course_dict, fileName="course_data.json", filePath=os.path.join(current_path, 'course'))
        # Check if the response indicates a successful course creation
        if(response["acknowledged"]):
            self.courses.append(course_obj)
            print(f"Course {course_dict['course_name']} (Code: {course_dict['course_code']}) created with instructor {course_dict['insturctor']}.")

        
    def enroll_in_course(self, student_id, course_code):
        existing_student = StudentManagementSystem.record_exists(self.students, "student_id", student_id)
        existing_course = StudentManagementSystem.record_exists(self.courses, "course_code", course_code)

        if existing_student and existing_course:
            existing_student.enroll_course(existing_course)
            return
        # Print appropriate error messages based on the missing record
        if not existing_student:
            print("Error:: Enrollment failed. No student found with the provided student ID.")
        
        if not existing_course:
            print("Error:: Enrollment failed. No course found with the provided course code.")

        
    def add_grade(self, student_id, course_code, grade):
        existing_student = StudentManagementSystem.record_exists(self.students, "student_id", student_id)
        existing_course = StudentManagementSystem.record_exists(self.courses, "course_code", course_code)

        if existing_student and existing_course:
            existing_student.add_grade(existing_course, grade)
            return
        # Print appropriate error messages based on the missing record
        if not existing_student:
            print("Error:: Enrollment failed. No student found with the provided student ID.")
        
        if not existing_course:
            print("Error:: Enrollment failed. No course found with the provided course code.")
    
    
    def display_student_details(self, student_id):
        existing_student = StudentManagementSystem.record_exists(self.students, "student_id", student_id)
        if existing_student:
            existing_student.display_student_info()
            return
        print(f"Error:: Student ID {student_id} doesn't exist.")
    
    
    def display_course_details(self, course_code):
        existing_course = StudentManagementSystem.record_exists(self.courses, "course_code", course_code)
        if existing_course:
            existing_course.display_course_info()
            return
        print(f"Error:: Course {course_code} doesn't exist.")
         
  
    @staticmethod
    def record_exists(records, searchKey, searchValue):       
        for record in records:
           if (record.__dict__)[searchKey] == searchValue:
               return record
        return None
    
    
    @staticmethod
    def dictToObject(list, class_name):
        return [class_name(**dict) for dict in list]
            
    
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
0. Exit
"""
    print(mainMenu)
    option = input("Select Option: ")
    return option
    
while True:
    print()
    option = display_menu()
    
    if option == "1":
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        address = input("Enter Address: ")
        student_id = input("Enter Student ID: ")
        sms.add_student(name, age, address, student_id)
    
    elif option == "2":
        course_name = input("Enter Course Name: ")
        course_code = input("Enter Course Code: ")
        instructor = input("Enter Instructor Name: ")
        sms.add_course(course_name, course_code, instructor)

    elif option == "3":
        student_id = input("Enter Student ID: ")
        course_code = input("Enter Course Code: ")
        sms.enroll_in_course(student_id, course_code)
    
    elif option == "4":
        student_id = input("Enter Student ID: ")
        course_code = input("Enter Course Code: ")
        grade = input("Enter Grade: ")
        sms.add_grade(student_id, course_code, grade)
    
    elif option == "5":
        student_id = input("Enter Student ID: ")
        sms.display_student_details(student_id)
    
    elif option == "6":
        course_code = input("Enter Course Code: ")
        sms.display_course_details(course_code)
    
    elif option == "0":
        print("Exiting Student Management System. Goodbye!")
        exit()
        
    else:
        print("Error:: Invalid Option Selected. Please Try Again a Valid Choice.")
    
    