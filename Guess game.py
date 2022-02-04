import random
r = random.randint(0,10)
i = 0
a = eval(input("Guess a number between 0 and 10: "))
while r != a and i < 4:
    if a == (-9):
        r = a
    if i < 4 and (a < r or a > r):
        print("You still have ", (3-i), "attempts.")
    if a < r:
        print("Higher number")
        a = eval(input("Guess a number between 0 and 10: "))
    elif a > r:
        print("Lower number")
        a = eval(input("Guess a number between 0 and 10: "))
    i = i + 1
if r == a:
    print("CONGRATULATIONS")
if r != a:
    print("You have exceeded the number of attempts")