LIST_OF_WORDS = ["apple", "trip","rest",
                 "read", "good", "right",
                 "ex", "high",
                 "sir", "slow", "even", "that", "full",
                 "how", "salad", "come", "us",
                 "all", "haze", "rim", "pull",
                 "rum", "pee","burp"]

WORD_LIST_TFILE = "wordslist.txt"
SCORE_FILE = "scores.txt"

import random
from turtle import *
import turtle

def score_write(word):
    ''' function random_list_of_words
        parameters: void
        returns: nothing

        does: Creates a textfile of words from the list of words stored
        in a list in memory and places on disk.
    '''
    try:
        
        outfile = open(SCORE_FILE, "w")
        outfile.write(word + '\n')
        outfile.close()

    except OSError:
        print("Error trying to write file")




def random_list_of_words():
    ''' function random_list_of_words
        parameters: void
        returns: nothing

        does: Creates a textfile of words from the list of words stored
        in a list in memory and places on disk.
    '''
    try:
        
        outfile = open(WORD_LIST_TFILE, "w")
        for word in LIST_OF_WORDS:
            outfile.write(word + '\n')
        outfile.close()

    except OSError:
        print("Error trying to write file")
        

def create_dict_words():
    '''  function create_dict_words
         parameters: void
         returns: dictionary

         does: reads list of words into dictionary from a
         text file.
    '''

    dictionary = {}
    line_num = 1
    try: 
        infile = open(WORD_LIST_TFILE, "r")
        words = infile.readlines()
        for word in words:
            dictionary[line_num] = word.strip()
            line_num += 1
        infile.close()
        return dictionary
    
    except OSError:
        print("Error reading text file")


def random_word():
    '''  function random_word
         parameters: void
         returns: string

         does: selects a random word from a dictionary of words. 
    '''
    random_list_of_words()
    words = create_dict_words()
    rand_word = random.choice(words)
    return rand_word


def list_for_checking_for_item(item):
    '''  function list_for_checking_for_item
         parameters: string
         returns: list

         does: turns a string into a list of characters 
    '''
    test_list = []
    
    for i in item:
         test_list.append(i)

    return test_list



def rocket_body():
    ''' function rocket_body
         parameters: void
         returns: nothing

         does: draws the shape of rockets body using turtle
    '''
    word_turtle = Turtle()
    word_turtle.hideturtle()
    
    word_turtle.penup()
    word_turtle.goto(0,175)
    word_turtle.pendown()
    word_turtle.goto(-50,100)
    word_turtle.goto(-50,-100)
    word_turtle.goto(50,-100)
    word_turtle.goto(50,100)
    word_turtle.goto(0,175)


def left_rocket():
    '''  function left_rocket
         parameters: void
         returns: nothing

         does: draws the shape of rockets left side using turtle
    '''
    word_turtle = Turtle()
    word_turtle.hideturtle()
    
    word_turtle.penup()
    word_turtle.goto(-70,-50)
    word_turtle.pendown()
    word_turtle.goto(-40,-130)
    word_turtle.goto(-100,-130)
    word_turtle.goto(-70,-50)


def left_flame():
    '''  function left_flame
         parameters: void
         returns: nothing

         does: draws the shape of rockets left flame using turtle
    '''
    word_turtle = Turtle()
    word_turtle.hideturtle()

    word_turtle.penup()
    word_turtle.goto(-100,-130)
    word_turtle.pendown()
    word_turtle.goto(-90,-150)
    word_turtle.goto(-80,-130)
    word_turtle.goto(-70,-160)
    word_turtle.goto(-60,-130)
    word_turtle.goto(-50,-150)
    word_turtle.goto(-40,-130)
    
def right_rocket():
    '''  function right_rocket
         parameters: void
         returns: nothing

         does: draws the shape of rockets right side using turtle
    '''
    word_turtle = Turtle()
    word_turtle.hideturtle()
    
    word_turtle.penup()
    word_turtle.goto(70,-50)
    word_turtle.pendown()
    word_turtle.goto(40,-130)
    word_turtle.goto(100,-130)
    word_turtle.goto(70,-50)

def right_flame():
    '''  function right_flame
         parameters: void
         returns: nothing

         does: draws the shape of rockets flame using turtle
    '''
    word_turtle = Turtle()
    word_turtle.hideturtle()

    word_turtle.penup()
    word_turtle.goto(100,-130)
    word_turtle.pendown()
    word_turtle.goto(90,-150)
    word_turtle.goto(80,-130)
    word_turtle.goto(70,-160)
    word_turtle.goto(60,-130)
    word_turtle.goto(50,-150)
    word_turtle.goto(40,-130)


def draw_lines(lines):
    '''  function draw_lines
         parameters: int
         returns: nothing

         does: draws lines according to input value of lines
    '''
    word_turtle = Turtle()
    word_turtle.hideturtle()
    for i in range(lines):
        word_turtle.pendown()
        word_turtle.forward(20)
        word_turtle.penup()
        word_turtle.forward(10)

def draw_words(word, letter):
    '''  function draw_words
         parameters: string, string
         returns: nothing

         does: takes users letter and matches it to the
         approriate space 
    ''' 

    for i in range(len(word)):
        word_turtle = Turtle()
        word_turtle.hideturtle()
        word_turtle.penup()
        word_turtle.setpos(10 + 30 * (word[i]), 1)
        word_turtle.write(letter, move = True, align ='center', font = ('Arial', 15, 'normal'))


def check_count(count):
    '''  function check_count
         parameters: int
         returns: nothing

         does: takes user input int and determines which
         function should be ran according to its value
    ''' 
    
    if count == 1:
        rocket_body()
        
    elif count == 2:
        left_rocket()
    
    elif count == 3:
        left_flame()

    elif count == 4:
        right_rocket()
      
    elif count == 5:
        right_flame()

def game_play():
    ''' function game_play
        parameters: void
        returns: string

    does: takes user input string and returns the letter
    '''        
    guessed_letter = input("Guess a letter\n")
    guessed_letter = guessed_letter.lower()
    
    return guessed_letter

def turtle_reset():
    turtle.clearscreen()






          
