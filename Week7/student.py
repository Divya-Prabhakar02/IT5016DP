class Student():
    def __init__(self,name, age, studentid):
        self.name = name
        self.age = age
        self.studentid = studentid
        self.courses = []
    def enroll(self, courses):
        return(self.courses.append(courses))
    def drop(self, courses):
        return(self.courses.remove(courses))
    def get_info(self):
        print(f"Summary \n Name:{self.name} \n Age:{self.age} \n StudentID:{self.studentid} \n Courses: {self.courses}")

information = Student("Divya" , 22, 20240563)
information.enroll("software")
information.enroll("it")
information.drop("it")
information.get_info()
