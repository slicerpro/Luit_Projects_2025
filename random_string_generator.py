import random
import string

number_of_names = int(input("How many names do you want to generate? "))
department_names = input("What is the name of the department? ")

for i in range(number_of_names):
    random_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    print(f"{department_names}-{random_name}")
