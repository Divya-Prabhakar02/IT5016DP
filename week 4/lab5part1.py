def collect_user_data(id_counter):
    user_name = input("enter the name:")
    user_age = input("enter the age:")
    user_email = input("enter the email:")
    
    unique_id=id_counter +1
    updated_counter=unique_id

    print(f"User Information:\nName:{user_name}\nAge:{user_age}\nE-mail:{user_email}\nUnique ID:{unique_id}")
    return updated_counter, unique_id
    
id_counter=5000
id_counter, unique_id= collect_user_data(id_counter)






