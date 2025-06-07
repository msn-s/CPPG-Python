#Author:    Mason
#Created:   June 5th 2025
#Updated:   June 6th 2025
#Description:
# A program where the shop keeper can input and keep track of their sales, in sizes and quanitity
# the program will also display the percentage of what size shirt was sold in total to the rest
# using inputs 1-4 to indicate shirt size (S,M,L,XL) and "5" being a tally up all of the shirts sold and display
# which sizes and how many of each shirt were sold



# Constants
SHIRTS_SOLD         = "(As a whole number) Enter amount of shirts sold: "
EXIT_PROGRAM        = "\nPress enter to exit program...\n"
ERROR_INVALID_TYPE  = "\nError: Please input a whole number in range from 1-5\n"
ERROR_INVALID_RANGE = "\nError: Number must be a whole number between 1-5\n"
ERROR_NO_SALES      = "\n No shirts were sold today"
OPTION_1            = 1
OPTION_2            = 2
OPTION_3            = 3
OPTION_4            = 4
OPTION_5            = 5

# Variables
small         = 0
medium        = 0
large         = 0
xl            = 0
quantity      = 0
total_shirts  = 0
# Boolean that is set to True once user inputs "5" allows us to exit loop & program
close_program = False 
# Boolean that can keep us 
is_valid = False

# Stay in this main lopp until the user selects 5, flagging "close_program" as True
while close_program == False:    
    print("\n1: Small")
    print("2: Medium")
    print("3: Large")
    print("4: Extra Large")
    print("5: Tally & Exit")
    
    try:
        # Validation block for insuring user inputs 1-5
        user_choice = int(input("\nPlease enter number (1-5): ").strip())
        if 1 <= user_choice <= 5:
            is_valid = False 
            if user_choice == OPTION_1:
                # While they have not input a valid whole number representing shirts sold, redirect them back to the input 
                while not is_valid: 
                    print("Size small selected")       
                    quantity = input(SHIRTS_SOLD).strip()
                    # If they input a whole number, add it to total_shirts and the respective size shirt variable
                    if quantity.isnumeric():
                        quantity = int(quantity)
                        small += quantity
                        total_shirts += quantity
                        is_valid = True

                    else:
                        # Else if it is not numeric, or a whole number, print the error message
                        print(ERROR_INVALID_TYPE)
                is_valid = False     
            elif user_choice == OPTION_2:
                while not is_valid:
                    print("Size medium selected:")
                    quantity = input(SHIRTS_SOLD).strip()
                    if quantity.isnumeric():
                        quantity = int(quantity)
                        medium += quantity
                        total_shirts += quantity
                        is_valid = True

                    else:
                        print(ERROR_INVALID_TYPE)
                is_valid = False 
            elif user_choice ==  OPTION_3:
                while not is_valid:
                    print("Size large selected:")
                    quantity = input(SHIRTS_SOLD).strip()
                    if quantity.isnumeric():
                        quantity = int(quantity)
                        large += quantity
                        total_shirts += quantity
                        is_valid = True

                    else:
                        print(ERROR_INVALID_TYPE)
                is_valid = False 
            elif  user_choice == OPTION_4:
                while not is_valid:
                    print("Size extra-large selected:")
                    quantity = input(SHIRTS_SOLD).strip()
                    if quantity.isnumeric():
                        quantity = int(quantity)
                        xl += quantity
                        total_shirts += quantity
                        is_valid = True

                    else:
                        print(ERROR_INVALID_TYPE)

            elif user_choice ==  OPTION_5:
                # Validation to make sure we have sold more than 0 shirts
                if total_shirts > 0:
                # Set to true to exit while loop and program after it displays our math below
                    close_program = True 
                    print("Tally & Exit selected: \n")
                    
                    # Math to represent each percentage of shirt size sold in comparison to total shirts sold 
                    small_percentage = small / total_shirts * 100
                    medium_percentage = medium / total_shirts * 100
                    large_percentage = large / total_shirts * 100
                    xl_percentage = xl / total_shirts * 100
                    
                    # Formatting our print statements to mimic a table so it is easier for the user to read, with tabs and proper spacing
                    print("Size\t\tQty. \t%")
                    print(f"Small\t\t {small}\t{round(small_percentage,2)}%")
                    print(f"Medium\t\t {medium}\t{round(medium_percentage,2)}%")
                    print(f"Large\t\t {large}\t{round(large_percentage,2)}%")
                    print(f"Extra Large\t{xl}\t{round(xl_percentage,2)}%")
                else:
                    # If we have not sold any shirts today, exit the loop so we dont break the program trying to divide 0 
                    print(ERROR_NO_SALES)
                    close_program = True

        else:
            # Error if user inputs something outside of the scope 1-5
            print(ERROR_INVALID_RANGE)

    except ValueError:
        # Error if user inputs a string or something not numeric
        print(ERROR_INVALID_TYPE)
# Exit program
input(EXIT_PROGRAM)
