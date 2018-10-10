'''
CS5001
LAB2
FALL 2018
QINGJING GONG  & CASTON BOYD
'''

'''
We plan to travel to China, and we are writing this
project to help us pick some authentic chinese food. 

  Q1： Which Providence？
  a. Beijing
  b. Shanghai
  c. Sichuan

  Q2: Which flavor?
  a. spicy
  b. salty
  c. sweet

  Q3: Which type?
  a. meat
  b. vegetable
  c. dessert


  result example:

  a x a : Peking Roasted Duck
  a x b : fried mushroom
  a x c : mooncake
  b a x : manhan
  b (b or c) x: mooncake
  c x (a or b) : hot pot
  c x c : ice cream
  
'''


def main():

# Input for user's location choice, flavor choice, and food choice. 

    place = input("Which Providence? a. Beijing; b. Shanghai; c. Sichuan\n").casefold()
# if the user's input is invalid, then designate a valid value for user
    if (place != "a") and (place!= "b") and (place != "c"):       
        print("Input invalid. We choose a for you")
        place = "a"
    flavor = input("Which flavor do you prefer? a. spicy; b. salty; c. sweet\n").casefold()
# if the user's input is invalid, then designate a valid value for user
    if (flavor != "a") and (flavor!= "b") and (flavor != "c"):
        print("Input invalid. We choose a for you")
        flavor = "a"
    food = input ("Which type of food do you prefer? a.meat; b. vegetables; c. dessert\n").casefold()
# if the user's input is invalid, then designate a valid value for user
    if (food != "a") and (food != "b") and (food != "c"):
        print("Input invalid. We choose a for you")
        food = "a"
    
# Combination of user's choices.


    if place == "a" and food == "a":
        print("Peking Roasted Duck")
    elif place == "a" and food == "b":
        print("fried mushroom")
    elif place == "a" and food == "c":
        print("mooncake")
    elif place == "b" and flavor == "a":
        print("manhan")
    elif (place == "a") and (flavor == "b" or "c"):
        print("mooncake")
    elif (place == "c") and (food == "b" or "a"):
        print("hot pot")
    elif place == "c" and food == "c":
        print("ice cream")
    
    


main()
