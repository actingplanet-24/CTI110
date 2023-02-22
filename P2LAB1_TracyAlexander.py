mpg = float(input())
gascost = float(input())

milesA = float(20)
milesB = float(75)
milesC = float(500)


gallonsUsedA = milesA / mpg
gallonsUsedB = milesB / mpg
gallonsUsedC = milesC / mpg

travelcostA = gallonsUsedA * gascost
travelcostB = gallonsUsedB * gascost
travelcostC = gallonsUsedC * gascost


print(f'{travelcostA:.2f} {travelcostB:.2f} {travelcostC:.2f}')