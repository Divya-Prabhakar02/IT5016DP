def myfun(a,b):
    sum = a+b
    return sum 
def function1(a,b):
    addition = a+b
    return addition
def function2(a,b):
    subtracti1on = a-b
    return subtracti1on
def function3(a,b):
    multiply = a*b
    return multiply
def function4(a,b):
    divide = a/b 
    return divide
def main():
    a= int(input("enter the value for a:"))
    b =  int(input("enter the value for b:"))

    choice = int(input("Enter the function name"))
    if choice == 1:
        print(function1(a,b))
    elif choice ==2:
        print(function2(a,b)) 
    elif choice == 3:
        print(function3(a,b))
    else:
        print(function4(a,b))
main()        


