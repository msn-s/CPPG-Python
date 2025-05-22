#Author:    Mason
#Created:   May 22nd 2025
#Description:
# Outputting the total area of a horse track
# based on the users inputs provided
# Horse tracks are shaped of two rectnagles and two semi cirlces
# hence the calculation for semi circles, we add both together to get the area of both of them.
# we then take the rectangle area and square it as their are two rectangles.


#const

PI = 3.14159

#vars

rectangle_length = float(input("What is the length of one of the rectangles? "))
rectangle_width = float(input("What is the width of one of the rectangles? "))
rectangle_area = rectangle_length * rectangle_width * 2

inner_diameter = float(input("What is the inner diameter? "))
outer_diameter = float(input("What is the outer diameter? "))

inner_radius = inner_diameter / 2
outer_radius = outer_diameter / 2

circle_area = (PI * outer_radius * outer_radius) - (PI * inner_radius * inner_radius)
total_area = circle_area + rectangle_area

print(f" The total area of both semi circles is {circle_area} m². ")
print(f"The total area of both rectangles is {rectangle_area} m².")
print(f" Your total area is {total_area:.2f} m². ") 
# Outputting to two decimal places as we are working with meters squared in this case






