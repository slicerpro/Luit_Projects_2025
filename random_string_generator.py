import random
import string
import sys

number_of_names = int(input("How many names do you want to generate?\n"))
user_department = input("What is your department?: ")
department_names = ["Marketing", "Accounting", "FinOps"]


# Check if the department name is valid
if user_department not in department_names:
    
    print("You have entered an invalid department name\n\n")
   
else:
     print(f"The generated names are:\n")
    # Generate random names
     for i in range(number_of_names):
        random_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        print(user_department + "-" + random_name)
            
