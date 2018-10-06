'''
CS5001
HW3
craps.py
FALL 2018
CASTON BOYD
'''



'''
How did you make sure that, if the user runs out of money, you exit the program?
- The only time the user loses money is when he rolls. I have it that at the end
- Checked to see if the user's total is not less than or equal to zero
- Ran a test by hard coding the users money total to $0 if he rolled a draw
- I also harded coded money total to $0 if he loss 

How did you make sure that, after the dice are rolled, the bet re-sets to $10?
- I run three test playing a game with a win, draw, or loss:
- Immediately after each game, I select the print option to see bet total
- I also make sure that they aren't given $10 to bet if they have less than
- $10 after each game

How did you make sure that, if the user enters an invalid menu option, you prompt them again?
- I use different letters, numbers when prompted.
- I also try words that start with valid input letters
- Used repeated letters of valid input

How did you make sure that, if the user enters an invalid bet, you prompt them again?
- tried anything less than 1
- Tested input greater than the amount in the bank

How did you test for winning, both in the case of 7 and in the case of 11?
- Hard coded dice to 4 and 3
- Hard coded dice to 6 and 5

How did you test for losing, in the case of 2, 3, and 12?
- Hard coded dice to 1 and 1
- Hard coded dice to 2 and 1
- Hard coded dice to 6 and 6

'''

import time
import random


DEFAULT_BET_AMOUNT = 10
LUCKY_SET = [7, 11]
LOSING_SET = [2, 3, 12]

def main():
    # variables for starting cash, options letters and bet counter
    this_amount_left = 100
    options_list = ["P", "B", "R", "Q"]
    current_bet = 0

    # starts the game with default bet at $10
    if this_amount_left < 10:
        current_bet = this_amount_left
    else:
        current_bet = DEFAULT_BET_AMOUNT

    # while loop to run the game 
    while True:

        # This is the options for the user to select from
        print("\nLet's play some craps!")
        print("P: Print Status")
        print("B: Bet")
        print("R: Roll")
        print("Q: Quit")       
        choice_is = input("Choose one of the options\n").upper()

        # if user doesnt select "P", "B", "R", "Q"
        if choice_is not in options_list:
            print("Invalid entry. Try again")
            continue
        
        # Q: End the loop if the user chooses Q
        elif choice_is == options_list[3]:
                print("You had $" + str(this_amount_left) + " in the bank")           
                break

            
        # P: Print bank and current bet status
        # Also remind user of the rules to the game
        elif choice_is == options_list[0]:
                print("\n***Amount in the bank***: " "$" + str(this_amount_left))
                print("***Current betting power***: " "$" + str(current_bet))
                print("")
                print("")
                print("Remember 7 or 11, you win! 2, 3, or 12, you lose. "
                      "Anything else, it’s a draw.")
                time.sleep(1)

                
                    
        # B: The user can bet up to, but no more than,
        # the amount of money they have
        # They cannot bet less than $1.
        elif choice_is == options_list[1]:
                print("You have $" + str(this_amount_left))
                while True: 
                    users_bet_input = int(input("How much are you trying to bet?\n"))
                    if users_bet_input < 1:
                        print("You have to bet something. $0 wont work.")
                        time.sleep(0.5)
                        continue
                    elif users_bet_input > this_amount_left:
                           print("You have only $" + str(this_amount_left) +
                               "." " You dont have enough")
                           time.sleep(0.5)
                           continue
                    else:
                        current_bet = users_bet_input
                        print("You set your bet to $" + str(current_bet))
                        time.sleep(0.9)
                        break
                
            
        # R:  Roll the dice.
        # Generate two random values between 1 and 6 (inclusive)
        elif choice_is == options_list[2]:
               # two dice and the total together
               dice_one = random.randint(1,6)
               dice_two = random.randint(1,6)
               total_dice = dice_one + dice_two
               print("You rolled", dice_one, "and", dice_two)

               # total is 7 or 11
               if total_dice in LUCKY_SET:
                   this_amount_left = this_amount_left + current_bet
                   print("You win")
                   if this_amount_left >= 10:
                       current_bet = DEFAULT_BET_AMOUNT
                       
                   else:
                       current_bet = this_amount_left
                       
               # total is 2, 3, or 12
               elif total_dice in LOSING_SET:
                   this_amount_left = this_amount_left - current_bet
                   print("You lose")
                   # if the bank total is greater than or equal to $10
                   # user default bank total is set to $10
                   if this_amount_left >= 10:
                       current_bet = DEFAULT_BET_AMOUNT
                       
                   # if users amount is                       
                   else:
                       current_bet = this_amount_left
                       
               # total is any other number                       
               else:
                   print("It's a draw")
                   current_bet = DEFAULT_BET_AMOUNT
                   
        # checks how much is in the bank
        # if total is $0, program exits 
        if this_amount_left <= 0:
            print("You have $" + str(this_amount_left))
            time.sleep(0.8)
            print("You're broke! Out of the casino")
            break
            
main()
