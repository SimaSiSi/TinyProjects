"""
You could condense the code by leaving the assignment statements (line 9 - 11) out and putting them 
directly in the function (line 16 - 18), but I prefer it like this.

"""
import random as rdm
import string

lowers = string.ascii_lowercase
uppers = string.ascii_uppercase
digits = string.digits
punctuation= string.punctuation

def password_generator (numberofletters, numberofnumbers, numberofpunctuation):
    new_pw = []
    new_pw.extend(rdm.choice(lowers+uppers) for i in range(numberofletters))
    new_pw.extend(rdm.choice(digits) for i in range(numberofnumbers))
    new_pw.extend(rdm.choice(punctuation) for i in range(numberofpunctuation))
    rdm.shuffle (new_pw)
    print ('Your new password is:')
    print(''.join(str(i) for i in new_pw))

def create_a_random_pw ():
    print('There we go! I\'ll ask you something about the preferences of your new password. \nBear in mind that the sum of the characters constitutes also the total lenght of your password!')

    while True:
        try:
            letters = int(input('How many letters should there be in your generated password?\n'))
            nums = int(input('How many numbers should there be in your generated password?\n'))
            specialchars = int(input('How many special characters should there be in your generated password?\n'))
            break
        except:
            print ('Invalid value')
            continue

        

    password_generator (letters, nums, specialchars)

create_a_random_pw()
