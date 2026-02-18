## CODE FOR SAMPLE ASSIGNMENT

# C=float(input("ENTER TEMP IN CELSIUS: "))
# F=(9/5)*C+32
# print(F"{F:.2f}")

## NUMBER GUESSING GAME (SELF PROJECT)

import random
print("......NUMEBER GUESSING GAME........")
n=random.randint(1,100)
attempts=0
while True:
    guess= int(input("ENTER A NUMBER:"))
    attempts+=1
    if guess<n:
        print("TOO LOW: TRY AGAIN")
    elif guess>n:
        print("TOO HIGH: TRY AGAIN")
    else:
        print("YOU GUESSED IT")
        print("YOU GUESSED IT IN",attempts,"ATTEMPTS")
