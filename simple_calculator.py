# Author: Mason
# Created: May 29th 2025
# Description: 
# Calculating a single digit equation with our input provided
# It must only be 3 characters, use a valid operator, and have validation checks
# The program will output the calculation in form of #0# as instructed

# Constants
CLOSE_MESSAGE = "\n Press enter to exit...\n"

# Variables
equation = input("Enter a Single digit equation (e.g. 5+2): ")
# Initializing this variable. I am not sure if i have to, however 
# This will be used for error handling below
valid_equation = False 

# Check if the input has exactly 3 characters
if len(equation) == 3:
    # Check if the first and third characters are digits
    if equation[0].isdigit() and equation[2].isdigit():
        # Check if the middle character is a valid operator (+, -, *, /)
        if equation[1] in "+-*/":
            # Perform the calculation based on the operator, this is the case until line 38
            if equation[1] == "+":
                calculation = int(equation[0]) + int(equation[2])
                valid_equation = True
            elif equation[1] == "-":
                calculation = int(equation[0]) - int(equation[2])
                valid_equation = True
            elif equation[1] == "*":
                calculation = int(equation[0]) * int(equation[2])
                valid_equation = True
            elif equation[1] == "/":
                # Converting to int in order to check for 0 as an input in the equation.
                 # Validation check, never divide by 0! 
                if int(equation[2]) != 0:  
                    calculation = int(equation[0]) / int(equation[2])
                    valid_equation = True
                
                else:
                    # Error message if user divides by 0
                    print("Error: Cannot divide by zero.")
        else:
            # Error message if user inputs invalid operation
            print("Invalid operator! Only use (+, -, *, /).")
    else:
        # Error message if user inputs anything non-numeric on either side of the operator
        print("Non-numeric characters are not accepted at positions 0 or 2.")
else:
    # Error message if len() != 3 
    print("Invalid input. Ensure the equation 3 characters long and is in the form of this example (e.g. 5+2).")


# Print the calculation if the equation is valid ( i realized if i dont do this it crashes the program)
if valid_equation:
    print(f"Result: {calculation}")
else:
# Do not print the calculation if it doesent pass the checks, as it will crash!
    print("The equation is invalid, no result to display.")

# Closing message
input(CLOSE_MESSAGE)
