def student_details():
    items = {}
    student_info = int(input("enter keys and values in a dictionary."))
    for i in range (student_info): 
        registeration_number = input(f"enter the key of dictionary:{i+1}")
        first_name  = (input(f"enter the value in a dictionary:{i+1}"))
        items[registeration_number] = first_name
        return items

    
        
        
def main():
    student_details()
main()













