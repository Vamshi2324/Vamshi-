# 3. Create a Python project to guess a number that has randomly selected.

import random

Action = range(0, 101)


def player():
    while True:
        user_action = int(input(f"Guess a number from 0 to 100 : "))

        user_input = user_action
        if user_input not in list(Action):
            print(f"Invalid selection. Guess a value from 0 to 100")
            continue
        else:
            return user_action
        break
    ##player()


def computer():
    # randomly picks a number

    selection = random.randrange(0, 101)
    # print(selection)

    return selection


##computer()

def game():
    while True:
        user_selection = player()
        print("You guessed : ", user_selection)
        computer_selection = computer()
        print("Computer choose : ", computer_selection)

        if user_selection == computer_selection:
            print("You won!")
            break
        else:
            print("Try one more time!")
        continue


game()
