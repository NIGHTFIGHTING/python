import random

player = int(input("please input a number:"))

computer = random.randint(0,2)
#computer = random.random()

while true:
    if (player == 1 and computer == 0):
        print("you a winner")
