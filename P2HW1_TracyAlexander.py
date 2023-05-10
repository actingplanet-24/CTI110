#This program calculates travel expenses
#28 Feb 2023
#CTI-110 P2HW1 - Travel
#Alexnader Tracy
#
print("This program calculates and displays travel expenses")

budget = int(input("Enter Budget: "))

destination = str(input("Enter your travel destination:"))

gas = int(input("How much do you think you will spend on gas?"))

shelter = int(input("Approximately how much will you need for accomadation/hotel?"))

food = int(input("Last, how much do you need for food?"))

spent = (gas + shelter + food)

remainingbudget=(budget - spent)

print("------------Travel Expense------------")
print("Location:", " "*9, destination)
print("Initial budget:", " "*3, budget)
print("Fuel:", " "*13, gas)
print("Accomadations:", " "*4, shelter)
print("Food:", " "*13, food)
print("-"*38)
print(" ")
print("Remaining Balance: ", remainingbudget)