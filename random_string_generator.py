import random
import string

number_of_names = int(input("How many names do you want to generate?\n"))
user_department = input("What is your department?: ")
department_names = ["Marketing", "Accounting", "FinOps"]


for i in range(number_of_names):
        if user_department not in department_names:
            print("\nPlease enter a valid department name\n")
            break
        else:
            random_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
            print(user_department + "-" + random_name)
            
