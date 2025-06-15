'''
Instructions
Problem Description:

You are given the slope m and the y-intercept b of a line, along with a value x. Your task is to calculate and return the value of y using the equation of a line in slope-intercept form:

y=mx+b



Input:

Three floating-point numbers: slope, intercept, and x.



Output:

A floating-point number representing the value of y corresponding to the given x.



Example:

Input: slope = 2, intercept = 3, x = 4
Output: 11.0

Input: slope = 1.5, intercept = -2, x = 2
Output: 1.0
'''

def value_of_y(slope, b, x):
    y = slope * x + b
    return y

print(value_of_y(2, 3, 4))  # Output: 11.0
print(value_of_y(1.5, -2, 2))  # Output: 1.0