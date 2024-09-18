def function1():
    print("A")
    function2(3)
    print("B")
def function2(num):
    print("C")    
    function4(num-1, num-2)
    print("D")
def function3(number):
    print("E", number)
def function4(num1,num2):
    print("F")
    function3(num1+num2)
def main():    
    print("G")
    function1()
main()    