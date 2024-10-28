
class Course:
    
    def __init__(self, course_name, course_code, insturctor):
        self.course_name = course_name
        self.course_code = course_code
        self.insturctor = insturctor
        
    def add_student(self, student):
        pass
    
    def display_course_info(self):
        print("Course Information:")
        print("Course Name:", self.course_name)
        print("Code:", self.course_code)
        print("Instructor:", self.insturctor)
        
        

        