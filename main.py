import random

while True:
    print("  1. Roll The Dice              2. Exit")
    enduser = int(input("Choose Between the options : "))
    if enduser == 1:
        num = random.randint(1 , 6)
        print(num)
    else:
        break