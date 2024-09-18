def function1(num1,num2,num3):
    num1 = int(input("enter the first whole number"))
    num2 = int(input("enter the second whole number"))
    num3 = int (input("enter the third whole number"))
    sum = num1+num2+num3
    smallest = min(num1,num2,num3)
    bigger_total= sum-smallest
    return bigger_total
def main():
    print(1,function1(3,4,5))
    print(2, function1(11,23,34))
    print(3,function1(56,67,89))
main()    


