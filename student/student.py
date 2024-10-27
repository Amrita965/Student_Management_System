
from person.person import Person

class Student(Person):
    
    def __init__(self, name, age, address, student_id):
        super().__init__(name, age, address)
        self.student_id = student_id 
        
    def add_grade(self, subject, grade):
        pass
    
    def enroll_course(self, course):
        pass
    
    def display_student_info(self):
        pass
    