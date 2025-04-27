#Get loan details
money_owed = float(input("How much money do you owe in dollars?\n")) #50,000
apr = float(input("What is the annual interest rate of the loan?\n"))
payment = float(input("What is the monthly payment amount?\n"))
months = int(input("How many months do you want to see the results for?\n"))
monthly_interest_rate = apr / 100 / 12

for i in range(months):
    # calculate interest to pay
    interest_paid = monthly_interest_rate * money_owed
    # add in interest
    money_owed = money_owed + interest_paid
    # make payment
    money_owed = money_owed - payment
    if money_owed <= 0:
        print("You owe 0 dollars")
        print("You paid off your loan in", i + 1, "months.")
        break
print("You still owe", money_owed, "dollars after month", i + 1, ".", )
        
    

