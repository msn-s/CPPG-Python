#Author:    Mason Hilder
#Created:   May 16th 2025
#Description:
# Outputting information based on amount 
# of coffee sold during the week


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





#   scrapping this total_grounds = GRAMS_PER_CUP * (small_coffee * 1) + (medium_coffee * 2) + (large_coffee * 3) 
#   writing the code was not the issue for me, it was the word problem however so im just leaving that up there so you can see
#   the few processes i went through while, even simple math drives me nuts, however actually writing the word problem
#   down on paper and doing it step by step helped, the constants also kept everything very clean and simple to read.
#   without them i probably would have been VERY lost , so good practice thank you