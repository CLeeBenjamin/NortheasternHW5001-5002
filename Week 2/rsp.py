'''
CS5001
HW2
rsp.py
FALL 2018
CASTON BOYD
'''

import random

ROCK = "R"
PAPER = "P"
SCISSORS = "S"

#Test Case #1:
'''
Input:
S

Expected Output: 
You chose: S
Computer chose: R
You lose
'''

#Test Case #2
'''
Input:
P

Expected Output: 
You chose: P
Computer chose: P
It's a Tie 
'''

#Test Case #3
'''
Input:
S

Expected Ouput: 
You chose: S
Computer chose: P
You win
'''


def main():
    user_answer = input("R, S, or P?\n").upper()
    user_answer = user_answer.replace(' ', '')
  
    #Makes sure user input is not case sensitive
    if user_answer == "rock".upper() or user_answer == ROCK:
        user_answer = ROCK
        print("You chose:", user_answer)
    elif user_answer == "scissors".upper() or user_answer == SCISSORS:
        user_answer = SCISSORS
        print("You chose:", user_answer)      
    elif user_answer == "paper".upper() or user_answer == PAPER:
        user_answer = PAPER
        print("You chose:", user_answer)
    else:
        print("Wrong input. Try Again!")
        raise SystemExit() 

    #Computer Input: ROCK == 1, PAPER == 2, SCISSORS = 3    
    computer_input = random.randint(1, 3)
    if computer_input == 1:
        computer_input = "R".upper()
        print("Computer chose: R")
    elif computer_input == 2:
        computer_input = "P".upper()
        print("Computer chose: P")
    elif computer_input == 3:
        computer_input = "S".upper()
        print("Computer chose: S")

    #Conditions for when you win, when you lose, and when you tie
    if ((user_answer == ROCK and computer_input == SCISSORS) or
        (user_answer == PAPER and computer_input == ROCK) or
        (user_answer == SCISSORS and computer_input == PAPER)):
        print("You win")
    elif ((computer_input == ROCK and user_answer == SCISSORS) or
          (computer_input == PAPER and user_answer == ROCK) or
          (computer_input == SCISSORS and user_answer == PAPER)):
        print("You lose")     
    elif computer_input == user_answer:
        print("It's a tie")
    
main()
