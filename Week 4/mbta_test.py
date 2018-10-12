from mbta import is_valid_station
from mbta import get_direction
from mbta import get_num_stops



def check_valid_station_method(test_cases, expected):
    
    if expected == True:
        print("-Checking for valid directions: correct destination-")
    else:
        print("-Checking for invalid directions: incorrect destination-")
        
    passed_test = 0
    failed_test = 0


    for test in test_cases: 
        if expected == True:
            print("Tested stations", test,"is valid", end = '')
        elif expected == False:
            print("Tested station", test,"is invalid", end = '')


        if is_valid_station(test) == expected:
            passed_test += 1               
            print("...SUCCESS!")
            

        else:
            failed_test += 1
            print("...FAILURE")

    print("Passed:", passed_test, "Failed:", failed_test)
    print("\n")



def check_get_direction(station_one, station_two, expected):

    
    ashmont = "Ashmont"
    alewife = "Alewife"
    here = "You're at your destination"
    none_found = "no destination found"
    passed_test = 0
    failed_test = 0

    if expected == ashmont:
        print("-Checking for stations to Ashmont-")
    elif expected == alewife:
        print("-Checking for stations headed to Alewife-")
    elif expected == here:
        print("-Checking for same station to and from-")       
    else:
        print("-Checking for invalid directions: incorrect destination-")
    
    for i, j in zip(station_one, station_two):
        if expected == alewife:
            print("Tested", i, "to", j, "in direction to Alewife", end = '')
        elif expected == ashmont:
            print("Tested", i, "to", j, "in direction to Ashmont", end = '')
        elif expected == here:
            print("Tested", i, "to", j, end = '')
        elif expected == none_found:
            print("Tested", i, "and", j, "as invalid forms", end = '')

            
        if get_direction(i, j) == expected:
            passed_test += 1               
            print("...SUCCESS!")
        else:
           failed_test += 1
           print("...FAILURE")


    print("Passed:", passed_test, "Failed:", failed_test)
    print("\n")


def check_get_num_stops(station_one, station_two):

    for i in range(len(station_one)):

        print(station_one[i]) 
    ## find a way to subtract indices of two elements from
    ## test case list and compare that number to the method output of
    ## get_num_stops
            



    
def main(): 

    valid_stations = ["Ashmont", "Shawmut", "Fields Corner", "Savin Hill", "JFK/UMass",
            "Andrew", "Broadway", "South Station", "Downtown Crossing",
            "Park St", "Charles/MGH", "Kendall", "Central", "Harvard",
            "Porter", "Davis", "Alewife"]

    invalid_stations_names = ["Ashm0nt", "", "FIELDS Corner", "Savin HILL", "/UMass",
            "Andreew", "broadway", "SouthStation", "DowntownCrossing",
            "Park Street", "Charles MGH", "KendalL", "Cental", "Harvaard",
            "Porter  ", "DRvis", "Ale^wife"]

    stations = ["Ashmont", "Shawmut", "Fields Corner", "Savin Hill", "JFK/UMass",
            "Andrew", "Broadway", "South Station", "Downtown Crossing",
            "Park St", "Charles/MGH", "Kendall", "Central", "Harvard",
            "Porter", "Davis", "Alewife"]

    
    stations_minus_one = ["Shawmut", "Fields Corner", "Savin Hill", "JFK/UMass",
            "Andrew", "Broadway", "South Station", "Downtown Crossing",
            "Park St", "Charles/MGH", "Kendall", "Central", "Harvard",
            "Porter", "Davis", "Alewife"]

    direction_ashmont = ["Ashmont", "Shawmut", "Fields Corner", "Savin Hill", "JFK/UMass",
            "Andrew", "Broadway", "South Station", "Downtown Crossing",
            "Park St", "Charles/MGH", "Kendall", "Central", "Harvard",
            "Porter", "Davis"]
    stations_to_ashmont = direction_ashmont[::-1]

    ashmont_direction = ["Ashmont", "Shawmut", "Fields Corner", "Savin Hill", "JFK/UMass",
            "Andrew", "Broadway", "South Station", "Downtown Crossing",
            "Park St", "Charles/MGH", "Kendall", "Central", "Harvard",
            "Porter", "Davis", "Alewife"]
    station_to_ashmont = ashmont_direction[::-1]

    
##    check_valid_station_method(valid_stations, True)
##    check_valid_station_method(invalid_stations_names, False)
    
##    check_get_direction(stations, stations_minus_one, "Alewife")
##    check_get_direction(station_to_ashmont, stations_to_ashmont, "Ashmont")
##    check_get_direction(stations, stations, "You're at your destination")
##    check_get_direction(invalid_stations_names, invalid_stations_names, "no destination found")

    check_get_num_stops(station_to_ashmont,stations)

    
main()
