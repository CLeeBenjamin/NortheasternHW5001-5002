'''
    CS5001
    HW1
    part 1: pace.py
    FALL 2018
    CASTON BOYD
'''

'''
Test Case #1:
2k race, 4 hour and 10 minute:
    1.24 miles, 3:21:36 pace, 0.30 MPH

Test case #2:
20k race, 2 hours and 13 minutes:
    12.43 miles, 10:41 pace, 5.61 MPH

Test case #3:
10k race, 1 hour and 10 minutes(mins: 70):
    6.21 miles, 11:15 pace, 5.32 MPH

'''

def main():

    #Intro questions
    name = input("Pace Calculator here. What's your name?\n")
    print("Nice to meet you, " + name)

    #User Input: kilometers, hours, and mins
    kilometers_ran = int(input("How many kilometers did you run today?\n"))
    hours_ran = int(input("How many hours did it take?\n"))
    mins_ran = int(input("What about the minutes?\n"))

    #mark - input calculated
    
    #number of kilometers * 0.621 miles
    miles_ran = round(float(0.621371 * kilometers_ran), 2)

    #take the input hours ran * 60 (1hr=60mins) and add user minutes 
    total_time = round(float((hours_ran * 60) + mins_ran), 2)

    # Gives the pace (hours_ran * 60 + mins_ran) / miles_ran
    paced_time = float(total_time / miles_ran)
    
    #this will genertate a statment if pace time is an hour or more
    #this means if the runners pace is above an hour, we run this code
    
    if paced_time > 60.00:
          hours = int(paced_time // 60)
          minute = float(paced_time % 60)
          minutes = int(minute)
          seconds_converted = float(minute % 1) * 60
          seconds = int(seconds_converted)
          mph = format(60 / paced_time, ".2f")
        
          #the statements below based on the amount of hours
          #if one hour, it states "one hour" instead of "one hours"
          if hours > 1:
             print("You ran", miles_ran, "miles") 
             print("It took you", hours , "hours", minutes , "minutes and", seconds, "seconds per mile to get it done")
             print("Your miles per hour were:", mph)   
          else:
             print("You ran", miles_ran, "miles")
             print("It took you", hours , "hour", minutes , "minutes and", seconds, "seconds per mile to get it done")
             print("Your miles per hour were:", mph)
             
    #else it will generate a statements for minutes
    else:

        minutes  = int(paced_time)
        seconds_conversion = float(paced_time % 1) * 60
        seconds = int(seconds_conversion)
        mph = round(float(60 / paced_time), 2)

        
        print("You ran", miles_ran, "miles")
        print("It took you", minutes , "minutes and", seconds, "seconds per mile.")
        print("Your miles per hour were:", mph)
                     
    
main()


