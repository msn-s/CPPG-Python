#Author:    Mason
#Created:   May 22nd 2025
#Description:
# Outputting the total area of a horse track
# based on the users inputs provided
# Horse tracks are shaped of two rectnagles and two semi cirlces
# hence the calculation for semi circles, we add both together to get the area of both of them.
# we then take the rectangle area and square it as their are two rectangles.

#import library

import math
# Importing this library for an accurate constant of PI, which is needed for our area calculations

# Vars

rectangle_length = float(input("What is the length of one of the rectangles? "))
rectangle_width = float(input("What is the width of one of the rectangles? "))

inner_diameter = float(input("What is the inner diameter? "))
outer_diameter = float(input("What is the outer diameter? "))

rectangle_area = rectangle_length * rectangle_width * 2
# There are two rectangles, so we multiply the area of one rectangle, by 2

inner_radius = inner_diameter / 2
outer_radius = outer_diameter / 2
# Radius is needed for our semi circle area calculations, radius is the diameter / 2

circle_area = (math.pi * outer_radius * outer_radius) - (math.pi * inner_radius * inner_radius)
# This calculation is taking the outer semi circle area, subtract the inner semi circle area to get the total area of the outer semi cirlce
# Which is  PI * radius²
total_area = circle_area + rectangle_area
# Calculating the sum of circle area + rectangle area

print(f"The total area of both semi circles is {circle_area:.2f} m².") #not needed for final output
print(f"The total area of both rectangles is {rectangle_area:.2f} m².") #not needed for final output

print(f"\nThe total area of the horse track is {total_area:.2f} m². \n") 
# Outputting to two decimal places as we are working with meters squared in this case






