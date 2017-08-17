import random


name = input("What is your name? ")

answer = random.randint(1,100)
print(answer)
trial = 3

while trial:
    guess = int(input("Hi, " + name  + ". Type the number(1,100): "))

    if guess == answer:
        print("Correct!")
        break
    elif guess > answer:
        trial -= 1
        print("Too High!! " + str(trial) + "times left")
    elif guess < answer:
        trial -= 1
        print("Too Low!! " + str(trial) + "times left")

if trial == 0:
    print("The Answer was ", answer)

