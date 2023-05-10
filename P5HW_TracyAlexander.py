import random #imports rand function
# Math quiz with subtraction and addition portion with menu to choose until user is done.
# 29-APR-2023
# CTI-110 P5HW - Math Quiz
# Alexander Tracy
#

def plus(): #addition portion
    a = random.randint(1,100) #generates rand 2 numbers
    b = random.randint(1,100)
    c = a + b #creates answer
    print("   ", a)
    print(" + ", b)
    d = int(input("Enter your answer.")) #creates user selection
    if d == c: #math portion, fairly straight forward using if, while loop using if
        print("Congratulations, your answer is correct!")
    while d != c:
        if d < c:
            print("Sorry, your guess is too low, try again.")
            d = int(input())
        elif d > c:
            print("Sorry, your guess is too high, try again.")
            d = int(input())
        print("Congratulations, your answer is correct!")
def sub(): #subtraction portion
    a = random.randint(1,100) #generates rand 2 numbers
    b = random.randint(1,100)
    c = a - b
    print("   ", a)
    print(" - ", b)
    d = int(input("Enter your answer.")) #creates user selection
    if d == c: #math portion, fairly straight forward using if, while loop using i
        print("Congratulations, your answer is correct!")
    while d != c:
        if d < c:
            print("Sorry, your guess is too low, try again.")
            d = int(input())
        elif d > c:
            print("Sorry, your guess is too high, try again.")
            d = int(input())
        print("Congratulations, your answer is correct!")
def main(): #menu portion
    print("Welcome to Math quiz\n") #introduction part, nothing cool, accidentally made it unexitable at first cause i forgot "break"
    while True:
        print("MAIN MENU")
        print("-"*20)
        print("1. Adding random numbers")
        print("2. Subtracting random numbers")
        print("3. Exit")
        choice = int(input("\nPlease choose one of the menu options:")) #creates functional menu portion
        if choice == 1:
            plus()
        elif choice == 2:
            sub()
        elif choice == 3:
            print("Thank you for playing!")
            print("Bye!")
            break
        else:
            print("Please make a valid selection.")
main()