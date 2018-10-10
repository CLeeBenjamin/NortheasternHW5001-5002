from password import has_an_alphabet
from password import has_a_numeric_value
from password import has_a_special_char
from password import is_right_char_length



def check_for_alphabet(test_cases, expected_results):
    ''' Function: check_for_alphabet
        Input: Lists of strings to test, and a boolean for expected result
        Returns: Nothing
        Does: Executes has_an_alphabet with all inputs from the list,
        and tests if they match the expected results.
    '''
    
    if expected_results == True:
        print("-Checking for valid passwords: has an alphabet-")
    else:
        print("-Checking for invalid passwords: doesnt have an alphabet-")
    passed_test = 0
    failed_test = 0
    
    for test in test_cases: 
        if expected_results == True:
            print("Tested password", test,"is valid", end = '')
        elif expected_results == False:
            print("Tested password", test,"is invalid", end = '')

        
        if has_an_alphabet(test) == expected_results:
            passed_test += 1               
            print("...SUCCESS!")
            

        else:
            failed_test += 1
            print("...FAILURE")
            
    print("Passed:", passed_test, "Failed:", failed_test)
    print("\n")


def check_for_numbers(test_cases, expected_results):
    ''' Function: check_for_numbers
        Input: Lists of strings to test, and a boolean for expected result
        Returns: Nothing
        Does: Executes has_a_numeric_value for all inputs from the list,
        and presents if they match the expected results.
    '''
    if expected_results == True:
        print("-Checking for valid passwords: has a number-")
    else:
        print("-Checking for invalid passwords: doesnt have a number-")
    passed_test = 0
    failed_test = 0
    for test in test_cases: 
        if expected_results == True:
            print("Tested password", test,"is valid", end = '')
        elif expected_results == False:
            print("Tested password", test,"is invalid", end = '')

        
        if has_a_numeric_value(test) == expected_results:               
            passed_test += 1               
            print("...SUCCESS!")
            

        else:
            failed_test += 1
            print("...FAILED")

        
    print("Passed:", passed_test, "Failed:", failed_test)
    print("\n")

def check_for_special_char(test_cases, expected_results):
    ''' Function: check_for_special_char
        Input: Lists of strings to test, and a boolean for expected result
        Returns: Nothing
        Does: Executes has_a_special_char for all inputs from the list,
        and presents if they match the expected results.
    '''
    if expected_results == True:
        print("-Checking for valid passwords: has a special character-")
    else:
        print("-Checking for invalid passwords: no special character-")
    passed_test = 0
    failed_test = 0
    for test in test_cases: 
        if expected_results == True:
            print("Tested password", test,"is valid", end = '')
        elif expected_results == False:
            print("Tested password", test,"is invalid", end = '')

        
        if has_a_special_char(test) == expected_results:               
            passed_test += 1               
            print("...SUCCESS!")
        else:
            failed_test += 1
            print("...FAILED")

        
    print("Passed:", passed_test, "Failed:", failed_test)
    print("\n")


def check_for_word_length(test_cases, expected_results):
    ''' Function: check_for_word_length
        Inputs: Lists of strings to test, and a boolean for expected result
        Returns: Nothing
        Does: Executes is_right_char_length for all inputs from the list,
        and presents if they match the expected results.
    '''
    if expected_results == True:
        print("-Checking for valid passwords: length between 6 and 12-")
    else:
        print("-Checking for invalid passwords: length less than 6 or greater than 12-")
    passed_test = 0
    failed_test = 0
    for test in test_cases: 
        if expected_results == True:
            print("Tested password", test,"is valid", end = '')
        elif expected_results == False:
            print("Tested password", test,"is invalid", end = '')

        
        if is_right_char_length(test) == expected_results:               
            passed_test += 1               
            print("...SUCCESS!")
        else:
            failed_test += 1
            print("...FAILED")

        
    print("Passed:", passed_test, "Failed:", failed_test)
    print("\n")



def check_valid_passwords(test_cases, expected_result):
    '''  Function: check_valid_passwords
         Input: Lists of strings to test, and a boolean for expected result
         Returns: Nothing
         Does: Executes is_right_char_length for all inputs from the list,
         and presents if they match the expected results.
    '''
    print("-Checking for valid passwords-")
    passed_test = 0
    failed_test = 0
    
    for test in test_cases: 
        print("Tested", test, end = '')
        if has_an_alphabet(test) == expected_result and \
           has_a_numeric_value(test) == expected_result and \
           has_a_special_char(test) == expected_result and \
           is_right_char_length(test) == expected_result:

            passed_test += 1               
            print("...SUCCESS!")
        else:
            failed_test += 1
            print("...FAILED")


        
    print("Passed:", passed_test, "Failed:", failed_test)
    print("\n")

def check_invalid_passwords(test_cases, expected_result):
    ''' Function: check_invalid_passwords
        Input: Lists of strings to test, and a boolean for expected result
        Returns: Nothing
        Does: Executes is_right_char_length for all inputs from the list,
        and presents if they match the expected results.
    '''
    print("-Checking for invalid passwords-")
    passed_test = 0
    failed_test = 0
    
    for test in test_cases: 
        print("Tested", test, end = '')
        if has_an_alphabet(test) == expected_result or \
           has_a_numeric_value(test) == expected_result or \
           has_a_special_char(test) == expected_result or \
           is_right_char_length(test) == expected_result:
            
            passed_test += 1               
            print("...SUCCESS!")
        else:
            failed_test += 1
            print("...FAILED")


    print("Passed:", passed_test, "Failed:",failed_test)





def main():


    # all valid passwords
    one_alphabet = ["111&%T%343", "4345t&&&", "123p23$", "#####i4%", "*1232G5%("]
    one_number = ["afdaf3&&", "rere4^^^", "fdre%5^&(", "fadf6#@$", "$#@L7Ljf"]
    one_special = ["1111$11nn", "333%33ii", "1232$Tty", "rea^f4df", "4544%jjf"]
    six_tweleve_length = ["43&f123", "312H&%#", "3afaf&&&&&a", "34&&&&&ft", "123$$$for"]
    all_valid = one_alphabet + one_number + one_special + six_tweleve_length


    
    # all invalid passwords
    missing_alphabet = ["111&%%343", "4345&&&", "12323$", "#####4%", "*12325%("]
    missing_special = ["111111nn", "3333333ii", "1232Tty", "reafdf", "4543445jjf"]
    missing_number = ["afdaf&&", "rere^^^", "fdre%^&(", "fadf#@$", "$#@LLjf"]
    missing_length = ["43&f", "312H", "3afaf&&&&&adfafd", "34&&&&&&&dfdaddf", "123"]
    all_invalid = missing_alphabet + missing_special + missing_number + missing_length

    # valid tests 
    check_for_alphabet(one_alphabet, True)
    check_for_numbers(one_number, True)
    check_for_special_char(one_special, True)
    check_for_word_length(six_tweleve_length, True)
    check_valid_passwords(all_valid, True)

    # invalid tests 
    check_for_alphabet(missing_alphabet, False)
    check_for_numbers(missing_number, False)
    check_for_special_char(missing_special, False)
    check_for_word_length(missing_length, False)
    check_invalid_passwords(all_invalid, False)
    
    

    


main()
