RED_LINE = ["Ashmont", "Shawmut", "Fields Corner", "Savin Hill", "JFK/UMass",
            "Andrew", "Broadway", "South Station", "Downtown Crossing",
            "Park St", "Charles/MGH", "Kendall", "Central", "Harvard",
            "Porter", "Davis", "Alewife"]



def is_valid_station(station):

    if station in RED_LINE:
        return True
    else:
        return False


def get_direction(start, end):
    
    start_index = 0
    end_index = 0
    ashmont = "Ashmont"
    alewife = "Alewife"
    here = "You're at your destination"
    none_found = "no destination found"
        
    for i in range(len(RED_LINE)):

        if RED_LINE[i] == start:
             start_index = i 

        if RED_LINE[i] == end:
             end_index = i

    if (start not in RED_LINE) or \
          (end not in RED_LINE):
        return none_found
    
    elif start_index > end_index:
        return ashmont
    elif start_index < end_index:
        return alewife
    elif start_index == end_index:
        return here
    


def get_num_stops(start, end):
    
    start_index = 0
    end_index = 0
        
    for i in range(len(RED_LINE)):

        if RED_LINE[i] == start:
             start_index = i 

        if RED_LINE[i] == end:
             end_index = i

    num_stops = abs(int(start_index - end_index))

    if (start not in RED_LINE) or \
          (end not in RED_LINE) or \
        (start_index == end_index):
        return 0
    
    elif (start_index > end_index) or \
         (start_index < end_index):
         return num_stops
    

