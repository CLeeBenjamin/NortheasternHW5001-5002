from spaceship import random_word
from spaceship import list_for_checking_for_item
from spaceship import rocket_body
from spaceship import left_rocket
from spaceship import left_flame
from spaceship import right_rocket
from spaceship import right_flame
from spaceship import draw_lines
from spaceship import draw_words
from spaceship import check_count
from spaceship import game_play
from spaceship import turtle_reset
from spaceship import score_write

def game():
    
    points = 0
    word = random_word()
    word_count = len(word)
    tries = 0
    list_of_pos = []
    count = 0 
    already_guessed = []
    print(word)
    while tries < 5:
        draw_lines(word_count)
        
        guessed_letter = game_play()
        already_guessed.append(guessed_letter)
        
        
      
        char_lst = list_for_checking_for_item(word)
        word_pos = [i for i, pos in enumerate(word) if pos == guessed_letter]

        # check if guessed letter isn't in the random word
        if not word_pos:
            count += 1
            
        # check if guessed letter is in the random word
        elif len(word_pos) != 0:
            list_of_pos.append(word_pos)
        print(list_of_pos)
        # elif cases for drawing rocket based on # of incorrect guesses
        check_count(count)
    
        # number of incorrect attempts           
        draw_words(word_pos, guessed_letter)
        
        
        total_pos = [pos for sublist in list_of_pos for pos in sublist]
        
        if word_count == len(total_pos):
             points += 1
                   
             continue_game = input("Keep playing? Y/N\n").lower()
             if continue_game == "y":
                turtle_reset()
                continue
            
             elif continue_game == "n":
                user_name = input("what is your name?\n")
                score_write(user_name)
                raise SystemExit
                
        elif count == 5:
             print("you lose")
             print("the word was:",word)
             
             continue_game = input("Keep playing? Y/N\n").lower()
             if continue_game == "y":
                turtle_reset()
                continue
            
             elif continue_game == "n":
                user_name = input("what is your name?")
                score_write(user_name)
                raise SystemExit
        tries += 1
         
    continue_game = input("Keep playing? Y/N\n").lower()
    if continue_game == "y":
        turtle_reset()
        game()
            
    elif continue_game == "n":
        user_name = input("what is your name?")
        score_write(user_name)
        raise SystemExit


        
       
        
     
                 
                       
game()


    
    
