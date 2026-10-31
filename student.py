class Student:
    """Store student information."""
    def __init__(self,student_id,name,age,course):
        self.student_id=student_id
        self.name=name
        self.age=age
        self.course=course

    def display_details(self):
        """Display student information"""
        print("student ID:",self.student_id)   
        print("Name:",self.name)
        print("Age:",self.age)
        print("Course",self.course)


