#Author:    Mason
#Created:   May 16th 2025
#Description:
# Outputting information about the total mL's
# and total coffee grounds(grams) used at the end of the week
# based on the inputs provided using our formulas.



#constants
ML_PER_CUP      = 250
GRAMS_PER_CUP   = 10


#vars
small_coffee = int(input("Enter the amount of small coffees sold this week as a whole number. "))
medium_coffee = int(input("Enter the amount of medium coffees sold this week as a whole number. "))
large_coffee = int(input("Enter the amount of large coffees sold this week as a whole number. "))
total_cups = (small_coffee * 1) + (medium_coffee * 2 ) + (large_coffee * 3)
total_ml = total_cups * ML_PER_CUP
total_grounds = total_cups * GRAMS_PER_CUP
print(f"The total amount of mL's of coffee sold this week was {total_ml} mL's")
print(f"The shop used {total_grounds} grams of coffee grounds this week")