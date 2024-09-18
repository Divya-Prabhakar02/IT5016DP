def username():
    studentID = str(input("Enter the student id:"))
    first_name = str(input("Enter the first name:"))
    last_name =  str(input("Enter the last name :"))
    university = str(input("what is the name of your university?"))
    
    #if  "WHITECLIFFE"  in university and "COLLEGE" in university :
    username = studentID[0:2]+last_name[0:3]
    print(f"Welcome to the whitecliffe college. Your username is {username} ")
    #else:
    print("please enter your university and generate your username.")

def main():
    print(username())            
main()    


      





