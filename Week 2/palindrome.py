'''
CS5001
HW2
palindrome.py
FALL 2018
CASTON BOYD
'''


#Test Case #1:
'''
Test Case #1: white space/palindrome
m   o   m
expected output: it is a palindrome
'''
#Test Case #2:
'''
Test case #2: whitespace/nonpalindrome
j   a  n e
expected outcome: it is not a palindrome
'''
#Test Case #3:
'''
Test case #3: lowercase/palindrome
kayak
expected outcome: it is a palindrome
'''
#Test Case #4:
'''
Test case #4: lowercase/nonpalindrome
mike
expected outcome: it is not a palindrome
'''
#Test Case #5:
'''
Test case #5: uppercase palindrome
RACECAR
expected outcome: it is a palindrome
'''
#Test Case #6:
'''
Test case #6: uppercase nonpalindrome
NASCAR
expected outcome: it is not a palindrome
'''

#Test Case #7:
'''
Test case #7: Capitalized palindrome
Civic
expected outcome: it is a palindrome
'''
#Test Case #8:
'''
Test case #8: Capitalized nonpalindrome
NewDay
expected outcome: it is not a palindrome
'''
#Test Case #9:
'''
Test case #9: One Character
h
expected outcome: "h is not a long enough string.
'''

#Test Case #10:
'''
Test case #10: Special Characters
!!level!!
expected outcome: it is a palindrome
'''


def main():
    word = input("Enter a word.\n")
    users_word = word.casefold()
    users_word =  users_word.replace(' ', '')
    users_word_reverse =  users_word[::-1]
    
    #checks length of string
    if  len(users_word) >= 2:
        #if string is more than 1 character long, checks
        #if its a palindrom 
        if  users_word == users_word_reverse:
            print('"{}"'.format(word), "is a palindrome")
        #if not a palindrome
        else:
            print('"{}"'.format(word), "is not a palindrome")
    #if string is not more than 1 character
    else:
        print('"{}"'.format(word), "is not a long enough string.")
    

   

main()
