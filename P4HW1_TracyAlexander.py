# CTI-110
# P4HW1 - Score List
# Alexander Tracy
# 11-Apr-2023

totaln = int(input("How many scores do you want to enter?"))

n, mylist =1,[]

while (True):
    if(len(mylist)==totaln):
        break
    print("Enter score #"+str(n)+": ", end="")
    score=int(input())
    if(score>100 or score<0):
        print("Invalid score entered.\nPlease enter a valid score between 0 and 100.")
    else:
        mylist.append(float(score))
        n+=1

low = min(mylist)

mylist.remove(low)

scoreAvg = sum(mylist)/len(mylist)

if(scoreAvg > 90):
    grade = "A"
elif(scoreAvg < 90 and scoreAvg >= 80):
    grade = "B"
elif(scoreAvg < 80 and scoreAvg >= 70):
    grade = "C"
elif(scoreAvg < 70 and scoreAvg >= 60):
    grade = "D"
else:
    grade = "F"

print("-"*14, "Results", "-"*11)
print("Lowest Score   :", low)
print("Modified List  :", mylist)
print("Scores Average :", scoreAvg)
print("Grade          :", grade)
print("-"*34)


