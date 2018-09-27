'''
    CS5001
    HW2
    haybale.py
    FALL 2018
    CASTON BOYD
'''

#Temp
BASE_PRICE = 9
MAX_TEMP = 75
MIN_TEMP = 40
DEFAULT_TEMP = 75
MAX_TEST_TEMP = 99
MIN_TEST_TEMP = 0
#Money
TEN_CENT = .10
FIVE_CENT = .05
FIFTY_CENT = .50
TWO_DOLLAR = 2
ONE_DOLLAR = 1
#Rain
ITS_RAINING = True
#Time
LATEST_HOUR = 23
EARLIEST_HOUR = 0
MID_HOUR = 12
AFTER_FIVE = 17



#Test Cases #1: Above Max Temp
'''
temp = 90
day = mon
time = 15
raining = N
price = $10.50
'''

#Test Cases #2: Below Min Temp
'''
temp = 25
day = wed
time = 15
raining = N
price = $8.25
'''

#Test Cases #3: Wrong Day
'''
temp 54
day = what wed
time = 15
raining = N
price = $9.00

temp 54
day = sunday
time = 15
raining = N
price = $9.00
'''

#Test Cases #4: Weekday before/after 5pm
'''
temp = 54
day = wed
time = 14
raining = N

output: 
price = $9.00

temp = 54
day = wed
time = 19
raining = N

output:
price = $11.00
'''

#Test Cases #5: Weekends
'''
temp = 54
day = sun
time = 20
raining = N

output: 
price = $10.00

temp = 54
day = sat
time = 20
raining = N

output:
price = $10.00
'''

#Test Cases #6: Raining
'''
temp = 54
day = sun
time = 20
raining = Y

output:
price = $9.50
'''
#Test Cases #7: High Temp
'''
temp = 100
day = wed
time = 20
raining = N

output:
price = $11.00
'''

#Test Cases #8: Low Temp
'''
temp = -5
day = sun
time = 20
raining = N

output:
price = $10.00
'''

#Test Cases #9: Highest Price
'''
temp = 99
day = mon
time = 20
raining = N

output:
price = $13.40
'''


#Test Cases #10: Lowest
'''
temp = 0
day = mon
time = 11
raining = Y

output:
price = $6.50
'''

#Test Cases #11: Random
'''
temp = 80
day = tues
time = 11
raining = N

output:
price = $9.50

temp = 78
day = thurs
time = 14
raining = N

output:
price = $9.30
'''

def main():
    '''
    Ask For Temperature
    Day, Hour, and If Its Raining
    ''' 
    #temp
    temp = int(input("What is the current temp?\n"))
    #If the temperature entered by the user is less than 0 or greater than 99, default value 75
    if temp > MAX_TEST_TEMP or temp < MIN_TEST_TEMP:
        temp = DEFAULT_TEMP

    
    #day
    day = input("What day of the week is it?\n")
    if ((day != ("mon")) and (day != ("tues")) and (day != ("wed")) and
        (day != ("thur")) and (day != ("fri")) and (day != ("sat")) and
        (day != ("sun"))):
        day = "mon"
    else:
        day = day
        
    #hour
    hour = int(input("Time of the day. Enter a whole number from 0-23 for the current hour of the day.\n"))
    if hour > LATEST_HOUR or hour < EARLIEST_HOUR:
        hour = MID_HOUR
        
    #rain
    raining = input("Is it raining? Y/N\n")
    if raining == "Y":
        raining = ITS_RAINING
    else:
        raining = False

    
    '''
    Check if temp is above max temp or
    Below min temp
    '''
    #If the temperature is over 75 degrees, add 10 cents for every degree over 75.
    if temp > MAX_TEMP:
        add_for_temp = float(((temp - MAX_TEMP) * TEN_CENT) + BASE_PRICE)
        base_price = add_for_temp

    #If the temperature is under 40 degrees, subtract 5 cents for every degree under 40.
    elif temp < MIN_TEMP:
        subtract_for_temp = float(BASE_PRICE - ((MIN_TEMP - temp) * FIVE_CENT))
        base_price = subtract_for_temp

    else:
        base_price = BASE_PRICE

    '''
    Check for Weekday after 5 or
    Weekend 
    '''
    
    #If its a weekday after 5, add 2 dollars 
    if (((day == ("mon")) or (day == ("tues")) or (day == ("wed")) or
         (day == ("thur")) or (day == ("fri"))) and hour >= AFTER_FIVE):
        
        base_price = float(base_price + TWO_DOLLAR)

    #If its a weekend, add 1 dollar 
    elif (day == ("sat")) or (day == ("sun")):
         base_price = float(base_price + ONE_DOLLAR)

    '''
    Check if it raining
    '''
                 
    #If its raining, Subtract 50 cents
    if raining == ITS_RAINING:
        base_price = format(base_price - FIFTY_CENT,  ".2f")
    else:
        base_price =  format(base_price, ".2f")
        
    '''
    Final Price
    '''
    #Print Final Price
    print("Your price for the maze is:", "$" + base_price)                      

        
    
main()
