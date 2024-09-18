def total_user_numbers():
    total = 0
    number = int(input("enter the number(0 to end):") )
    while number!= 0:
        total =  total +number 
        number = int(input("enter the number (0 to end ):"))
        print("Total", total)
def main():
    total_user_numbers()

main()
