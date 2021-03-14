import random

Action = ['R', 'P', 'S', 'L', 'V']

def player():
    # ask user to input objects
    # check if the input is valid
    # if the input is valid, return a string that represents the object
    # else print out error message and keep asking until getting a vaild input
    while True: 
        user_action = input(f"Enter a choice in {Action}: ")
    
        user_input = ", ".join(user_action)
        if user_input not in Action:   
            print(f"Invalid selection. Enter a value in {Action}")
            continue
        else:    
            return user_action
        break    

def computer():
    # randomly picks an object and return the string

    
    selection1 = random.choices(Action)
    selection = ", ".join(selection1)  
    
    return selection
  

def game():
    # return True if player wins else False
    # if a tie happens, the process is repeated until a winner is found
    # print out messages for each round
    # print out winner if found and return bool
    while True :
        user_selection = player()
        print("You choose : ",user_selection)  
        computer_selection = computer()
        print("Computer choose : ",computer_selection) 
        
        if user_selection == computer_selection:
            print("It's a tie!")
            continue
            
        elif user_selection == "R":
            if computer_selection == "S":
                print("Rock crushes Scissor! You win!")
                return True
            elif computer_selection == "P":
                print("Paper covers rock! You lose.")
                return False
            elif computer_selection == "L":
                print("Rock crushes Lizard! You win!")
                return True
            else:
                print("Spock vaporizes Rock! You lose.")
                return False
                
        elif user_selection == "P":
            if computer_selection == "R":
                print("Paper covers rock! You win!")
                return True
            elif computer_selection == "S":
                print("Scissors cuts Paper! You lose.")
                return False
            elif computer_selection == "L":
                print("Lizard eats Paper! You lose.")
                return False    
            else:
                print("Paper disproves Spock! You win!")
                return True
        elif user_selection == "S":
            if computer_selection == "P":
                print("Scissors cuts paper! You win!")
                return True
            elif computer_selection == "R":
                print("Rock crushes Scissor! You lose.")
                return False
            elif computer_selection == "L":
                print("Scissors decapitates Lizard! You win!")
                return True    
            else:
                print("Spock smashes Scissors! You lose.")
                return False
        elif user_selection == "L":
            if computer_selection == "P":
                print("Lizard eats Paper! You win!")
                return True
            elif computer_selection == "R":
                print("Rock crushes Lizard! You lose.")
                return False
            elif computer_selection == "S":
                print("Scissors decapitates Lizard! You lose.")
                return False    
            else:
                print("Lizard poisons Spock! You win!")
                return True
        elif user_selection == "V":
            if computer_selection == "P":
                print("Paper disproves Spock! You lose.")
                return False
            elif computer_selection == "R":
                print("Spock vaporizes Rock! You win!")
                return True
            elif computer_selection == "S":
                print("Spock smashes Scissors! You win!")
                return True    
            else:
                print("Lizard poisons Spock! You lose.")
                return False
        break


print(game())
