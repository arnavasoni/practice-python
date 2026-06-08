import random

# computer picks a number between 1 and 9
comp = random.randint(1, 9)


while True:
    guess = input("Enter a number between 1 & 9 or type 'exit' to quit: ")
    if guess.lower() == 'exit':
        break
    elif int(guess) == comp:
        print("Exactly right!")
    elif int(guess) < comp:
        print("Too low")
    else:
        print("Too high")
