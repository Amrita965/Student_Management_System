
class Course:
    
    def __init__(self, course_name, course_code, insturctor, students = []):
        self.course_name = course_name
        self.course_code = course_code
        self.insturctor = insturctor
        self.students = students
        
    def add_student(self, student):
        self.students = [*self.students, student]
     
    def display_course_info(self):
        print("Course Information:")
        print("Course Name:", self.course_name)
        print("Code:", self.course_code)
        print("Instructor:", self.insturctor)
        print("Enrolled Students:", end=" ")
        for student in self.students:
            print(f"{student.name}", end=", ")

        
        

        