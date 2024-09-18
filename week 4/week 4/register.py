def student_details():
    items = {}
    student_info = int(input("Enter the number of entries you want to add to the dictionary: "))
    
    for i in range(student_info): 
        registration_number = input(f"Enter the registration number (key) for student {i+1}: ")
        first_name = input(f"Enter the first name (value) for student {i+1}: ")
        
        # Add the key-value pair to the dictionary
        items[registration_number] = first_name
    
    return items  # Return the dictionary after the loop completes

def main():
    # Call the function and store the returned dictionary
    student_data = student_details()
    
    # Print the dictionary
    print("\nStudent Registration Data:")
    print(student_data)

main()
