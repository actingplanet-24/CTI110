#CTI-110
#P2HW2 - List
#Alexander Tracy
#9-Mar-2023
#


module1 = float(input("Enter grade for Module 1:"))
module2 = float(input("Enter grade for Module 2:"))
module3 = float(input("Enter grade for Module 3:"))
module4 = float(input("Enter grade for Module 4:"))
module5 = float(input("Enter grade for Module 5:"))
module6 = float(input("Enter grade for Module 6:"))

modules = [module1, module2, module3, module4, module5, module6]
modulesaverage = sum(modules)/6


print("------------Results------------")

print(min(modules))
print(max(modules))
print(sum(modules))
print(modulesaverage)
print("-"*39)