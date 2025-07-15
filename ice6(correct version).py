#---------------------------------------------------------------------
# Author: Mason Hilder
# Date July 15th, 2025
# Purpose: A program that takes password as user input and validates it 
# through 6 different functions that return if password is valid or not, 
# while implementing constants for ease of use for admin
#---------------------------------------------------------------------

#region IMPORTS
#endregion

#region GLOBAL VARIABLES (CONSTANTS)
# YOU MAY NOT CHANGE ANYTHING IN THIS SECTION
# except for the values of the variables for testing purposes
MIN_PASSWORD_LENGTH = 8     
MAX_PASSWORD_LENGTH = 12    
ALLOW_SPECIAL_CHARACTERS = True 
ALLOWED_SPECIAL_CHARACTERS = "!@#$%^&*"
MUST_HAVE_DIGIT = True 
MUST_HAVE_UPPERCASE = True
MUST_HAVE_LOWERCASE = True
ALLOW_SPACES = False 
ALPHANUMERIC_CHARACTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
#endregion

#region FUNCTION DEFINITIONS
def validatePassword(password):
    '''A Wrapper function that sets flag to false if any of the validation functions return false'''
    isValid = True
    if not test_password_length(password):              isValid = False
    if not test_password_allowed_characters(password):  isValid = False
    if not test_password_must_have_digit(password):     isValid = False
    if not test_password_must_have_uppercase(password): isValid = False
    if not test_password_must_have_lowercase(password): isValid = False
    if not test_password_allow_spaces(password):        isValid = False
    return isValid

def test_password_length(password):
    '''A function that validates given argument checking its length to see if it is in valid range'''
    length = len(password)
    if length >= MIN_PASSWORD_LENGTH and length <= MAX_PASSWORD_LENGTH:
        return True
    else:
        return False

def test_password_allow_spaces(password):
    '''A function that checks for spaces in given password, checks if ALLOW_SPACES is true or not'''
    if " " in password:
        if ALLOW_SPACES:
            return True
        else:
            return False
    return True

def test_password_allowed_characters(password):
    '''A function that checks for each char in passsword, checks for special characters
    returns True or False given on the constants boolean value'''
    for c in password:
        if c in ALPHANUMERIC_CHARACTERS:
            continue
        elif ALLOW_SPECIAL_CHARACTERS and c in ALLOWED_SPECIAL_CHARACTERS:
            continue
        else:
            return False
    return True


def test_password_must_have_lowercase(password: str):
    '''A function that checks every char in password for lowercase, and if lowercase is allowed'''
    if MUST_HAVE_LOWERCASE:
        has_lowercase = False
        for c in password:
            if c.islower():
                has_lowercase = True
        return has_lowercase
    else:
        return True
    

def test_password_must_have_uppercase(password: str):
    '''A function that checks every char in password for uppercase, and if uppercase is allowed'''
    if MUST_HAVE_UPPERCASE:
        has_uppercase = False
        for c in password:
            if c.isupper():
                has_uppercase = True
        return has_uppercase
    else:
        return True


def test_password_must_have_digit(password: str):
    '''A function that checks every char in password for a digit, and returns value based on the MUST_HAVE
    DIGITs value'''
    for character in password:
        if character.isdigit():
            if MUST_HAVE_DIGIT:
                return True
            else:
                return False
def passwordsMatch(password1, password2):
    '''Returns if password1 is equal to password2 (checking if they are matching) returns value'''
    return password1 == password2

def getString(prompt):
    '''Returns string'''
    return input(prompt)

#endregion

#region MAIN APPLICATION

# YOU MAY NOT CHANGE ANYTHING IN THIS REGION
print('-'*40)
print("Welcome to the Password Generator")

doContinue = True
while doContinue:
    print('-'*40)

    # input
    password = getString("Enter your password (Q to Quit): ")
    if password.upper() == "Q":
        doContinue = False
        continue

    # have the user re-type the password to confirm
    password2 = getString("Re-enter your password: ")

    # check if the passwords match
    if passwordsMatch(password, password2):

        # check if the password is valid
        if validatePassword(password):    
            print("Password is valid")
        else: 
            print("Passwords are invalid")
    else:
        print("Passwords do not match")

    input("Press Enter to continue...")

print("Goodbye!")
print('-'*40)
exit(0)
#endregion