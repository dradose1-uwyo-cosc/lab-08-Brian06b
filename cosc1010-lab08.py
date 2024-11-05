# Brian Barrios Montiel
# UWYO COSC 1010
# November 4, 2024
# Lab 08
# Lab Section: 11
# Sources, people worked with, help given to:
# your
# comments
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 
def strings(a):
    if a.isdigit() or (a.startswith('-') and a[1:].isdigit()):
        return int(a)
    if a.count('.') == 1:
        try:
            float_value = strings(a)
            return float_value
        except ValueError:
            return False
    return False
        




print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

def slope_intercept(m, b, lower_x_bound, upper_x_bound):
    if not isinstance(lower_x_bound, int) or not isinstance (upper_x_bound, int):
        return False
    
    y_values = []
    for x in range(lower_x_bound, upper_x_bound + 1):
        y = m * x + b
        y_values.append(y)
    return y_values

while True:
    number_m = input("Enter the slope (m) or type 'exit to quit: ")
    if number_m.lower() == 'exit':
        break
    number_b = input("Enter the intercept (b) or type 'exit' to quit: ")
    if number_b.lower() == 'exit':
        break
    lower_x_input = input("Enter the lower x bound or type 'exit' to quit: ")
    if lower_x_input.lower() == 'exit':
        break
    upper_x_input = input("Enter the upper x bound or type 'exit' to quit: ")
    if upper_x_input.lower() == 'exit':
        break

    m = strings(number_m)
    b = strings(number_b)
    lower_x_bound = strings(lower_x_input)
    upper_x_bound = strings(upper_x_input)

    if m is False or b is False or not isinstance(lower_x_bound, int) or not isinstance(upper_x_bound, int):
        print("invalie Input. Enter numbers for m, b, and bounds.")
        continue

    result = slope_intercept(m, b, lower_x_bound, upper_x_bound)
    print("Resulting y values", result)


print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null
import math

def quadratic_formula(a, b, c):
    discriminant = b**2 - 4 * a * c
    

    if discriminant < 0:
        return None
    sqrt_discriminant = math.sqrt(discriminant)
    root1 = (-b + sqrt_discriminant) / (2 * a)
    root2 = (-b - sqrt_discriminant) / (2 * a)
    return root1, root2

while True:
    a_input = input("Enter value of a or type 'exit' to quit: ")
    if a_input.lower() == 'exit':
        break
    b_input = input("Enter value of b or type 'exit' to quit: ")
    if b_input.lower() == 'exit':
        break
    c_input = input("Enter value of c or type 'exit' to quit: ")
    if c_input.lower() == 'exit':
        break
    a = strings(a_input)
    b = strings(b_input)
    c = strings(c_input)

    if a is False or b is False or c is False:
        print("Invalid Input. Please enter a whole number.")
        continue
    result = quadratic_formula(a, b, c)
    if result is None:
        print("no real solution.")
    else:
        root1, root2 = result
        print(f"The roots are: {root1} and {root2}")

