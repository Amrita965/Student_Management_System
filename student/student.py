
from person.person import Person
from datetime import datetime
from utilities.student_utilites import loadDataFromJSONFile
import os
current_path = os.getcwd()
import json

class Student(Person):
    
    def __init__(self, name, age, address, student_id, courses=[]):
        super().__init__(name, age, address)
        self.student_id = student_id 
        
        if(courses):
            self.courses = courses
        
    def add_grade(self, subject, grade):
        pass
    
    def enroll_course(self, course):
        
        print(self.__dict__)
        
        fileName="student_data.json" 
        filePath=os.path.join(current_path, 'student')
        fullPath = os.path.join(filePath, fileName)
        current_student = self.__dict__
        
        enrollment_date = datetime.today().strftime("%Y-%m-%d")
        
        enrollment_info  = {
            "course_code": course.course_code,
            "course_name": course.course_name,
            "enrollment_date": enrollment_date,
            "status": "enrolled"
        }
        
        if 'courses' in current_student:
            
            for enrolledCourse in current_student['courses']:
                if enrolledCourse['course_code'] == course.course_code:
                    print(f"Error:: Student {self.student_id} is already enrolled in course {course.course_name}.")
                    return
                      
            current_student['courses'] = [
                *current_student['courses'],
                enrollment_info
            ]
            self.courses = [*self.courses, enrollment_info]
        else:
            current_student['courses'] = [
                enrollment_info
            ]
            self.courses = [enrollment_info]
        
        records = loadDataFromJSONFile(filePath=filePath, fileName=fileName)
        rest_records = list(filter(lambda record: record["student_id"] != self.student_id, records))
        with open(fullPath, 'w') as fp:
            json.dump([current_student, *rest_records], fp, indent=4)
        
        print(f"Student {self.student_id} has been enrolled in course {course.course_name}.")
            
    def display_student_info(self):
        print("Student Information:")
        print(f"Name: {self.name}")
        print(f"ID: {self.student_id}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")
        
        if hasattr(self, 'courses'):
            print("Enrolled Courses:")
            print("------------------------------------------------------------")
            
            for course in self.courses:
                print("Course Name: ", course['course_name'])
                print("Course Code: ", course['course_code'])
                print("------------------------------------------------------------")


    