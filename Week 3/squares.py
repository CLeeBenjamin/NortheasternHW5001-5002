'''
CS5001
HW3
squares.py
FALL 2018
CASTON BOYD
'''

import turtle
import random

def main():
    i = 0
    size = 100
    count = 0
    square = turtle.Turtle()
    square.speed(20)
    screen = turtle.Screen()
    screen.bgcolor("black")
        
  # list for colors        
    color_list = ["green", "blue", "orange", "purple", "red"]
    
    # for loop, creates 20 squares 
    for i in range(20):
        square.color(color_list[i % len(color_list)])
        # square for every square
        for i in range(4):
              square.forward(size)
              square.right(90)
              
        # directed angle by 20 after square is created
        square.right(20)
         
main()

    
