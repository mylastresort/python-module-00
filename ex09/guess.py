from random import randint

if __name__ == '__main__':
    tries = 0
    num = randint(1, 99)
    print("This is an interactive guessing game!\n\
    You have to enter a number between 1 and 99 to find out the secret number.\n\
    Type 'exit' to end the game.\n\
    Good luck!\n")
    while True:
        try:
            guess = input("What's your guess between 1 and 99?\n>> ")
            if (guess == 'exit'):
                break
            guess = int(guess)
            tries += 1
            if (guess == num):
                print(
                    "Congratulations, you've got it!\nYou won in %s attempts!" % tries)
                break
            print('Too high!' if guess > num else 'Too low!')
        except ValueError:
            print("That's not a number.")
        except (IOError, KeyboardInterrupt, Exception):
            break
