class Whitecliffe():
    def __init__(self,studentid, lname,program):
        self.studentid = studentid
        self.lname = lname
        self.program = program
        self.membershipid = 400001
    def member(self):
        self.lname = input("Enter the last name ")
        self.studentid = int(input("Enter the student ID"))
        self.program = input("Enter the program ")        
        self.membershipid+=1
        return self.membershipid
class Member():
    def __init__(self):
        self.registeredstudents = 400
        self.withdrwanstudents = 600
        self.active = True

    def withdraw(self):
        if self.active:
            self.registeredstudents-=1
            self.withdrwanstudents+=1
            print(f"Registered students ={self.registeredstudents} ")
            print(f"Withdrwan students = {self.withdrwanstudents} ")
        else:
            print("Invalid choices")
    def program(self,stream):
        if stream == "Diploma":
            print("Student Program is Diploma.")
        else:
            print("Student program is Bachelor")

    def display(self):
        print(f"Last name : {self.lname}")
        print(f"Member ship ID: {self.id}")
        print(f"Registered students: {self.registeredstudents}")
        print(f"Withdrwan students:{self.withdrwanstudents}")
info = Member("Prabhakar")
info.id(400)
info.withdraw()
info.display()
