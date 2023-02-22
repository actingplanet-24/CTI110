#Travel expenses calculator in python
#18/Feb/2023
#CTI-110 P1HW2
#Alexander Tracu

print("Please enter the budget for the trip")
budget = int(input())

print("What is the destination of the trip")
dest = input()

print("Enter how much will you be spending on gas?")
gasCost = int(input())

print("Enter how much you will be spending on accommodations")
accoCost = int(input())

print("Enter how much you will be spending on food")
foodCost = int(input())

totalCost = (foodCost + accoCost + gasCost)
finalBudget = (budget - totalCost)

print("Location:", dest)
print("Initial Budget:", budget)
print("Fuel:", gasCost)
print("Accomadation", accoCost)
print("Food:", foodCost)
print("Remaining Balance:", finalBudget)