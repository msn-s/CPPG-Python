# Author: Mason
# Created: June 9th 2025
# Description: 
# Taking the input of the given diamater of a pizza, and outputting the area per slice 
# As well as how many slices can be cut, given the diameter from the user

# Libraries
import math

# Constants
CLOSE_PROGRAM   = "Succesfully exited the program.\n"
ERROR_TYPE      = "\nERROR: Please input a numeric whole number only\n"
ERROR_RANGE     = "\nERROR: Please input a whole number between 8-24\n"
SIX_PROMPT      = f"Cut in 6 slices results in an area of"
EIGHT_PROMPT    = f"Cut in 8 slices results in an area of"
TEN_PROMPT      = f"Cut in 10 slices results in an area of"
TWELVE_PROMPT   = f"Cut in 12 slices results in an area of"
SIXTEEN_PROMPT  = f"Cut in 16 slices results in an area of"
DIAMETER_PROMPT = f"\nPizza Diameter: "

# Variables
exit_program = False

# Exit program is only set to "True" if user inputs "0" 
while not exit_program:  
    # Input handling
    diameter = input("Please enter the diameter of your pizza between 8-24\" (0 to end program): ").strip()
    # Numeric validation: if "True", continue
    if diameter.isnumeric():
        # Take our string and convert it to integer if string was a numeric whole number  
        diameter = int(diameter)  
        # While exit program is not selected, run this code below
        if not diameter == 0:
            # Math for caluclating area based on users input, divided by amount of slices
            if diameter >= 8 and diameter <= 24:
                # Calculations
                radius = diameter / 2
                area = math.pi * radius*radius
                six_slices     = area / 6
                eight_slices   = area / 8
                ten_slices     = area / 10
                twelve_slices  = area / 12
                sixteen_slices = area / 16
                # Range checking, as well as printing math accordingly to what range the diameter is
                if diameter >= 8 and diameter < 10:
                    print(f"{DIAMETER_PROMPT} {diameter}")
                    print(f"{SIX_PROMPT} {round(six_slices,2)}” per slice.\n")          
                elif diameter >= 10 and diameter < 14:
                    print(f"{DIAMETER_PROMPT} {diameter}")
                    print(f"{SIX_PROMPT} {round(six_slices,2)}” per slice.")  
                    print(f"{EIGHT_PROMPT} {round(eight_slices,2)}” per slice.\n")    
                elif diameter >= 14 and diameter < 16:
                    print(f"{DIAMETER_PROMPT} {diameter}")
                    print(f"{SIX_PROMPT} {round(six_slices,2)}” per slice.")   
                    print(f"{EIGHT_PROMPT} {round(eight_slices,2)}” per slice.")    
                    print(f"{TEN_PROMPT} {round(ten_slices,2)}” per slice.\n")           
                elif diameter >= 16 and diameter < 20:
                    print(f"{DIAMETER_PROMPT} {diameter}")
                    print(f"{SIX_PROMPT} {round(six_slices,2)}” per slice.")   
                    print(f"{EIGHT_PROMPT} {round(eight_slices,2)}” per slice.")    
                    print(f"{TEN_PROMPT} {round(ten_slices,2)}” per slice.")  
                    print(f"{TWELVE_PROMPT} {round(twelve_slices,2)}” per slice.\n")                
                elif diameter >= 20 and diameter <= 24:
                    print(f"{DIAMETER_PROMPT} {diameter}")
                    print(f"{SIX_PROMPT} {round(six_slices,2)}” per slice.")   
                    print(f"{EIGHT_PROMPT} {round(eight_slices,2)}” per slice.")    
                    print(f"{TEN_PROMPT} {round(ten_slices,2)}” per slice.")  
                    print(f"{TWELVE_PROMPT} {round(twelve_slices,2)}” per slice.") 
                    print(f"{SIXTEEN_PROMPT} {round(sixteen_slices,2)}” per slice.\n")    
            # Error handling  ("input whole number in valid range")       
            else:
                print(ERROR_RANGE)
        # If 0 is selected, Exit program and print exit message
        else:
            print(CLOSE_PROGRAM)
            exit_program = True
    # Error handling (input whole number only)          
    else:
        print(ERROR_TYPE)