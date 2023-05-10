#Alexander Tracy
#CTI-110-0901
#17 Mar 2023
#P3Lab (Leap Year)

input_year = int(input())

if((input_year % 400 == 0) or
   (input_year % 100 > 0) and
   (input_year % 4 == 0)

    ):
    print(input_year, "- leap year")
else:
    print(input_year, '- not a leap year')
print()