def has_an_alphabet(password):
    ''' Function: has_an_alphabet
        Parameters: password, a string
        Returns: bool, deteremines if string
        contains an alphabet letter
        Does: Iterates through each character
        and checks to see if it is an alphabet letter
    '''
    alphabet_list = []
    
    for i in password:
        if i.isalpha():
            alphabet_list.append(i)                       
            
    if len(alphabet_list) >= 1:
        return True
    else:
        return False
            
    

def has_a_numeric_value(password):
    ''' Function: has_a_numeric_value
        Parameters: password, a string
        Returns: bool, deteremines if string
        contains an alphabet letter
        Does: Iterates through each character
        and checks to see if it is an alphabet letter
    '''
    digit_list = []
    
    for i in password:
        if i.isdigit():
            digit_list.append(i)
            
    if len(digit_list) >= 1:
        return True
    else:
        return False
            
    

def has_a_special_char(password):
    ''' Function: has_a_special_char
        Parameters: password, a string
        Returns: bool, deteremines if string
        contains an alphabet letter
        Does: Iterates through each character
        and checks to see if it is an alphabet letter
    '''
    chars = {'~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-',
             '"', '*', '|', ',', '&', '<', '`',
             '}', '.', '_', '=', ']', '!', '>', ';',
             '?', '#', '$', ')', '/'}
    
    check_character = []
    
    for i in password:
        if i in chars:
            check_character.append(i)
                           
    if len(check_character) >= 1:
        return True

    else:
        return False



def is_right_char_length(password):
    ''' Function: is_right_char_length
        Parameters: password, a string
        Returns: bool, determines if string
        is accurate length
        between 6 and 12 characters long
        Does: checks if string length is greater than
        or equal to 6 and less than or equal to 12
    '''

    if len(password) >= 6 and len(password) <= 12:
        return True

    else:
        return False


