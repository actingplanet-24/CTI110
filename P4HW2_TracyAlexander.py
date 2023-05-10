#CTI-110
#P4HW2 - Salary Calculator
#Alexander Tracy
#23-Apr-2023
n = 1
ot = 1.5
tototpay = 0
totregpay = 0
totgp = 0
othrs = "hi"
hours = 0

while (True):
    print("Enter employee's name or \"Done\" to terminate:")
    name = input()
    if name == "Done":
        break
    else:
        n += 1
    
        print("How many hours did ", name, "work?")
        hours = int(input())
        print("What is the pay rate of", name, "?")
        rate = float(input())
        if hours > 40:
            othrs = hours - 40
            reghours = hours - othrs
        else:
            reghours = hours

        
        otrate = rate * ot

        regpay = rate * reghours
        otpay = othrs * otrate
        gpay = reghours + otpay

        totregpay += regpay
        tototpay += otpay
        totgp += gpay
        print("Employee name: ", name)
        print("\nHours worked", " "*2, "Pay Rate", " "*3, "OverTime", " "*3, "OverTime Pay", " "*5, "RegHour Pay", " "*6, "Gross Pay")
        print("-"*100)
        print(hours, " "*12, rate, " "*7, otrate, " "*9, otpay, " "*13, "$", regpay, " "*10, "$", gpay)

print("Total number of employees entered:", n)
print("Total amount paid for overtime:", tototpay)
print("Total amount paid for regular hours:", totregpay)
print("Total amount paid in gross:", totgp)
