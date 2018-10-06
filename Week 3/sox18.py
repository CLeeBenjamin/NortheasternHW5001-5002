'''
CS5001
HW3
sox18.py
FALL 2018
CASTON BOYD
'''



def main(): 

    record = [ 'W', 'W', 'W', 'W', 'L', 'W',
                      'W', 'W', 'L', 'W', 'W', 'W',
                      'W', 'W', 'W', 'W', 'W', 'L', 
                      'L', 'L', 'W', 'W', 'L', 'L',
                      'W', 'W', 'L', 'W', 'L', 'W', 'W',
                      'W', 'L', 'L', 'W', 'L', 'W',
                      'W', 'L', 'L', 'W', 'W', 'L', 'W',
                      'W', 'W', 'W', 'L', 'W', 'W',
                      'L', 'W', 'W', 'W', 'L', 'L', 'W',
                      'W', 'W', 'W', 'L', 'L', 'W', 'L',
                      'W', 'W', 'W', 'W', 'W', 'L', 'L',
                      'L', 'W', 'L', 'W', 'W', 'L',
                      'W', 'W', 'W', 'W', 'L', 'W',
                      'L', 'W', 'W', 'W', 'W', 'W',
                      'W', 'W', 'W', 'W', 'W', 'L', 'W',
                      'W', 'W', 'W', 'L' ]
    runs = [ 4, 1, 3, 2, 7, 4, 3, 10, 8, 14, 7, 6, 7, 10,
                   3, 10, 9, 8, 7, 0, 1, 3, 4, 5, 3, 6, 4, 10,
                   6, 5, 5, 5, 6, 6, 2, 6, 5, 3, 5, 5, 5, 3, 6,
                   5, 6, 6, 5, 4, 4, 3, 6, 8, 1, 8, 8, 6, 2, 3, 5, 9, 
                   6, 7, 2, 0, 4, 2, 2, 6, 5, 2, 6, 0, 9, 2, 1, 
                   9, 14, 2, 5, 9, 9, 4, 1, 11, 1, 4, 11, 3, 10,
                   15, 7, 5, 8, 4, 6, 7, 6, 5, 1, 0 ]
    
    # number of elements in runs' list
    runs_list_len = len(runs)
    # counters for wins, losses, zero and ten+ runs
    win_counter = 0
    loss_counter = 0
    zero_runs_counter = 0
    ten_plus_counter = 0

    # lists to hold wins, losses, and 
    win_index_number = []
    lose_index_number = []
    win_number = []
    win_number_total = []
    lose_number = []
    lose_number_total = []


    # if item in list is W or L, it counts accordingly
    for i in record:
        if i == "W":
            win_counter += 1
            
        elif i == "L":
            loss_counter += 1

    # adds all the items in the list and divides by
    # number of elements in the list
    total_added_run = sum(runs)
    runs_average = float(total_added_run / runs_list_len)

    # counts number of zeros and tens or greater in the list
    for i in range(runs_list_len):
        if int(runs[i]) == 0:
            zero_runs_counter += 1
            
        elif int(runs[i]) >= 10:
            ten_plus_counter += 1
            
    # takes index position of runs equal to 1 and runs greater than 10
    # appends those elements to a seperate list for use later
    for indx, num in enumerate(runs):
            if num == 1:
               win_index_number.append(indx)
               print(win_index_number)

            elif num >= 10:
               lose_index_number.append(indx)
               print(lose_index_number)
              
    # compares index position of win_index_number and lose_index_number to
    # indexes in record in that position
    # once the index is match, it is then placed in a separte list
    # these separate lists are used to give a count for:
    # games won with only 1 run and games lost with 10 or more runs 
    for indxs, value in enumerate(record):
            if indxs in win_index_number:
               win_number.append(value)

            elif indxs in lose_index_number:
               lose_number.append(value)
               

    # these separate lists are used to give a count for:
    # games won with only 1 run                 
    for i in win_number:
        if i == "W":
            win_number_total.append(i)
            
    # games lost with 10 or more runs            
    for i in lose_number:
        if i == "L":
            lose_number_total.append(i)
            

    
    
    print("Total Wins:", win_counter)
    print("Total Losses:",loss_counter)
    print("Average Runs:", runs_average)
    print("Games played with scored zero runs:", zero_runs_counter)   
    print("Games played with 10 or more runs:", ten_plus_counter)
    print("Games won with only 1 run:", len(win_number_total))
    print("Games lost with 10 or more runs:", len(lose_number_total))

main()
