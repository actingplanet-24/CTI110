# CTI-110
# P3HW2-Salary
# Alexander Tracy
# 20-Mar-2023

name = input("Enter employee's name:")
hrs = int(input("Enter number of hours worked:"))
hrly = float(input("Enter employee's pay rate:"))
print("-"*37)
RegPay = hrs * hrly
ot = hrs % 40
otpay = hrly * 1.5
gp = otpay + RegPay
print("Employee name: ", name)
print("\nHours worked", " "*2, "Pay Rate", " "*3, "OverTime", " "*3, "OverTime Pay", " "*5, "RegHour Pay", " "*6, "Gross Pay")
print("-"*100)
print(hrs, " "*12, hrly, " "*7, ot, " "*9, otpay, " "*13, "$", RegPay, " "*10, "$", gp)