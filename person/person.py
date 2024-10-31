
class Person:
    # Create Person class constructor to initialize person attributes
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    
    # Print all the details of the person
    def display_person_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")