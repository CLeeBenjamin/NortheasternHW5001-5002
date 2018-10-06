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
        
    color_list = ["green", "blue", "orange", "purple", "red"]
##    while count <= 20:
    for i in range(20):
        square.color(color_list[i%len(color_list)])
        for i in range(4):
              
              square.forward(size)
              square.right(90)
              print("I was here")   
        
        i +=i                           
        count += 1
        
        print("it went", count, "time through")
        square.right(20)

         
main()

    
