
from person.person import Person
from course.course import Course
from datetime import datetime
from utilities.student_utilites import loadDataFromJSONFile
import os
current_path = os.getcwd()
import json

class Student(Person):
    
    def __init__(self, name, age, address, student_id, courses=[], grades = {}):
        super().__init__(name, age, address)
        self.student_id = student_id 
        
        if(courses):
            self.courses = courses
            
        if(grades):
            self.grades = grades
            
        
    def add_grade(self, subject, grade):
        
        fileName="student_data.json" 
        filePath=os.path.join(current_path, 'student')
        fullPath = os.path.join(filePath, fileName)
        
        if hasattr(self, 'courses'):
            has_enrolled = False
            for enrolled_course in self.courses:
                if(enrolled_course['course_code'] == subject.course_code):
                    has_enrolled = True
            if has_enrolled:
                if hasattr(self, 'grades'):
                    self.grades = {
                        **self.grades,
                        subject.course_name: grade
                    }
                
                else:
                    self.grades = {
                        subject.course_name: grade
                    }
                    
                records = loadDataFromJSONFile(filePath=filePath, fileName=fileName)
        
                rest_records = list(filter(lambda record: record["student_id"] != self.student_id, records))
        
                with open(fullPath, 'w') as fp:
                    json.dump([self.__dict__, *rest_records], fp, indent=4)
                    
                print(f"Grade {grade} added for {self.name} in {subject.course_name}.")
            else:
                print("Error:: The student is not enrolled in this course. Unable to assign a grade.")
        else:
            print("Error:: The student is not enrolled in any courses. Please enroll in a course to proceed.")
        
    
    def enroll_course(self, course):
        
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
                
            self.courses.append(enrollment_info)
        else:
            current_student['courses'] = [
                enrollment_info
            ]
            self.courses = [enrollment_info]
        
        records = loadDataFromJSONFile(filePath=filePath, fileName=fileName)
        
        rest_records = list(filter(lambda record: record["student_id"] != self.student_id, records))
        
        with open(fullPath, 'w') as fp:
            json.dump([current_student, *rest_records], fp, indent=4)
        
        course.add_student(self)
        print(f"Student {self.student_id} has been enrolled in course {course.course_name}.")

 
    def display_student_info(self):
        print("Student Information:")
        print(f"Name: {self.name}")
        print(f"ID: {self.student_id}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")
        
        if hasattr(self, 'courses'):
            print("Enrolled Courses:", end=" ")
            for course in self.courses:
                print(course['course_name'], end=", ")
                
        if hasattr(self, 'grades'):
            print("\nGrades:", self.grades)



    