import random


name = input("What is your name? ")

answer = random.randint(1,100)
print(answer)
while True:
    guess = int(input("Hi, " + name  + ". Type the number(1,100): "))

    if guess == answer:
        print("Correct!")
        break
    else:
        print("You are wrong!!!!!!!!!!")

