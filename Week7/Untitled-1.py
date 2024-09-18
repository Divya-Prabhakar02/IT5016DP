class Whitecliffe():
    
    def __init__(self,stream):
        self.studentID = int(input("Enter the Student ID:"))
        self.lname = input("Enter the last nme of the students:")
        self.program = input("Enter the program(Bachelor/Diploma)")
        self.studentlist = []
        self.membershipcounter=1000
        self.withdrawnstudentscounter=400
        self.registeredstudentscounter=600
        self.bachelorstudents = 500
        self.diplomastudents=500
        self.stream = stream
    def membership(self):
        self.studentlist.append(self.lname)
        self.studentlist.append(self.studentID)
        self.membershipcounter+=1
        print(F"Hi {self.lname}, Your membership id is:{self.membershipcounter}")
        if self.stream.lower =="bachelor":
            self.bachelorstudents+=1
        elif self.stream.lower=="diploma":
            self.diplomastudents-=1
        else:
            print("Unknown Program, No any student in this Program.")
               
    def withdrawal(self):
        self.studentlist.remove(self.lname)
        self.studentlist.remove(self.studentID)
        self.registeredstudentscounter-=1
        self.withdrawnstudentscounter+=1
        print(f"Registered Number : {self.registeredstudentscounter} ")
        print(f"Withdrwal Students :{self.withdrawnstudentscounter}")
        self.stream= input("Enter the stream of the student")
        if self.stream.lower == "Diploma":
            print("The Student is in Diploma Program")
        else:
            print("The Student is in Bachelor Program")

        if self.stream.lower() =="bachelor":
            self.bachelorstudents-=1 
        elif self.stream.lower() =="diploma":
            self.diplomastudents-=1
        else:
            print("Invalid Stream:")

    def stastics(self):
        print(f"Number of registered students:{self.registeredstudentscounter}, {self.lname}")
        print(f"Students In Diploma Program :{self.diplomastudents}")
        print(f"Students in Bachelor Program :{self.bachelorstudents}")
        print(f"Number of students who have withdrawn their membership: {self.withdrawnstudentscounter}")
            
def main():
    system = Whitecliffe("diploma")
    while True:
            choice = input("\n 1.New Membership\n 2.Withdraw membership \n3.Stastics\n4.Exit ")

            if choice == "1":
                system.membership()
            elif choice == "2":
                system.withdrawal()
            elif choice == "3": 
                system.stastics()
            elif choice == "4":
                print("Existing Program")
                break
            else:
                print("Invalid Choice.")           
if __name__  == "__main__":
    main()            



