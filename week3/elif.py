def what_to_do():
    message = "Time to"
    prompt = "Enter selection(1,2 or 3):"
    user_choice = int(input(prompt))

    if user_choice == 1:
        print(message,"eat")
    elif user_choice ==2:
        print(message,"play")
    elif user_choice == 3:
        print(message ," sleep") 
    else:
        print("Incorrect Selection")    
what_to_do()           

