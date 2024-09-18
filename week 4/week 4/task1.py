def collect_user_information():
      counter_value = 5000
      return counter_value+1
    
user_name = input("ENTER THE NAME OF THE STUDENT:")
user_age = input("ENTER THE AGE OF THE USER:")
user_email = input("ENTER THE EMAIL OF THE USER:")
counter_value = 5000
unique_id_counter=collect_user_information()
print("user information:")
print(f"Name: {user_name}")
print(f"Age: {user_age}")
print(f"Email: {user_email}")
print(f"Unique_id:{unique_id_counter}")