# CTI-110-0901
#20-Mar-2023
# Alexander Tracy
# This program takes a number grade, determines the total average and displays letter grade for average.

# Enter grades for six modules

mod_1 = int(input('Enter grade for Module 1: '))
mod_2 = int(input('Enter grade for Module 2: '))
mod_3 = int(input('Enter grade for Module 3: '))
mod_4 = int(input('Enter grade for Module 4: '))
mod_5 = int(input('Enter grade for Module 5: '))
mod_6 = int(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades

low = min(grades)
high = max(grades)
total = sum(grades)
avg = (sum(grades)/len(grades))

# determine letter grade for average
print("------------Results------------")
print("Lowest Grade:", " "*5 , low)
print("Highest Grade: ", " "*3, high)
print("Sum of grades: ", " "*3, total)
print("Average: ", " "*9, avg)
print("-"*40)

if avg >= 90:
    print('Your average grade is: A')
elif avg >= 80:
        print('Your average grade is: B')
elif avg >= 70:
        print('Your average grade is: C') 
elif avg >= 60:
        print('Your average grade is: D')
else:
    print('Your grade is: F')





