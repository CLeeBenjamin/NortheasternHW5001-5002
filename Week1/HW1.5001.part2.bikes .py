'''
CS5001
HW1
part 2: bikes.py
FALL 2018
CASTON BOYD
'''

'''
Test Case #1:
Input: 1 Wheel, 2 Frames, 50 Links
Output: Program Ends
You do not have enough wheels to create a bike. Try again.

Test Case #2:
Input: 2 Wheels, 2 Frames, 50 Links
Output: 1 bike built. Wheels: 0, Frames: 1, Links: 0

Test Case #3:
Input: 5 Wheels, 4 Frames, Links: 150
Output: 2 bikes built. Wheels: 1, Frames: 2, Links: 50

Test Case #4:
Input: 4 Wheel, 1 Frames, 50 Links
Output: Program Ends 
You do not have enough frames to create a bike. Try again.

Test Case #5:
Input: 4 Wheel, 2 Frames, 50 Links
Output: Program Ends 
You do not have enough links to create a bike. Try again.

'''

def main():

    #wheels
    wheels = float(input("How many wheels do you have?\n"))
    
    if wheels >= 2:
        
        if wheels % 2 == 0:
            number_of_bikes = int(wheels // 2)
            if number_of_bikes <= 1:
                print("We can make", number_of_bikes, "bike with that amount.\n")
            else:
                print("We can make", number_of_bikes, "bikes with that amount.\n")
        else:
            number_of_bikes = int(wheels // 2)
            if number_of_bikes <= 1:
                print("We can make", number_of_bikes, "bike with that amount.\n")
            else:
                print("We can make", number_of_bikes, "bikes with that amount.\n")
    #system ends program if there is not adequate amount
    #of wheels per bike 
    else:
        print("You do not have enough wheels to create a bike. Try again.")
        raise SystemExit

    
    left_over_wheels = int(wheels - (number_of_bikes * 2))
    
    
    #frames
    frames = int(input("How many frames do you have?\n"))
    if frames >= number_of_bikes:
            if frames <= 1:
                print("We can make", frames, "bike with that amount.\n")
            else:
                print("We can make", frames, "bikes with that amount.\n")
        
    #system ends program if there is not adequate amount
    #of frames per bike     
    else:
        print("You do not have enough frames to create a bike. Try again.")
        raise SystemExit

    left_over_frames = int(frames - number_of_bikes)
        
    
    #links
    links = float(input("How many links do you have?\n"))

    if links >= (number_of_bikes * 50):
        if links % 50 == 0:
            bike_amount = int(links // 50)

            if bike_amount <= 1:
                print("We can make", bike_amount, "bike with that amount.\n")
            else:
                print("We can make", bike_amount, "bikes with that amount.\n")
                
        else:
            bike_amount = int(links // 50)
            
            if bike_amount <= 1:
                print("We can make", bike_amount, "bike with that amount.\n")
            else:
                print("We can make", bike_amount, "bikes with that amount.\n")

        left_over_links = int(links - (number_of_bikes * 50))
        
    #system ends program if there is not adequate amount
    #of links per bike 
    else:
        
        print("You do not have enough links to create a bike. Try again.") 
        raise SystemExit

    #number of bikes overall to make
    if number_of_bikes <= 1:
            print("We'll make", number_of_bikes, "bike for you")
    else:
            print("We'll make", number_of_bikes, "bikes for you")


    print("We'll keep the leftovers. Wheels:", left_over_wheels, " Frames:", left_over_frames, " Links:", left_over_links)
         

main()
