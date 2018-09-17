import math 

'''
Test Case #1:
3k race, 4 hour and 1 minute:
    1.86 miles, 2:9:34 pace, 6.11 MPH

Test case #2:
20k race, 2 hours and 13 minutes:
    12.42 miles, 10:42 pace, 7.01 MPH

Test case #3:
10k race, 1 hour and 17 minutes:
    6.21 miles, 12:23 pace, 10.96 MPH

'''



def main():

    name = input("Pace Calculator here. What's your name?\n")
    print("Nice to meet you, " + name)

    
    kilometers_ran = float(input("How many kilometers did you run today?\n"))
    hours_ran = int(input("How many hours did it take?\n"))
    mins_ran = int(input("What about the minutes?\n"))
    miles_ran = round(float(0.621371 * kilometers_ran), 2)

    

    total_time = round(float((hours_ran * 60) + mins_ran), 2)
    paced_time = float(total_time / miles_ran)
    
    
    if paced_time > 60.00:
          hours = int(paced_time // 60)
          minute = float(paced_time % 60)
          seconds_converted = float(minute % 1) * 60
          seconds = int(seconds_converted)
          minutes = int(minute)
          if hours > 1:
             print("Alright, it seems like it took you", hours , "hours", minutes , "minutes and", seconds, "seconds per mile to get it done")
          else:
             print("Alright, it seems like it took you", hours , "hour", minutes , "minutes and", seconds, "seconds per mile to get it done")
          
    else:
        hour_time = 0 
        minutes  = int(paced_time)
        seconds_conversion = float(paced_time % 1) * 60
        seconds = int(seconds_conversion)
        print("Alright, it seems like it took you", minutes , "minutes and", seconds, "seconds per mile to get it done")

                     
    
main()    
