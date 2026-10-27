# -------------------------------------------
# Advanced Python Challenge: Exercise 02 Operators and Conditionals
# -------------------------------------------

# Overview:
# This exercise challenges your understanding of Python operators, conditionals, and input handling.
# Complete each section with the required logic, using good variable names and adding comments where necessary.

# -------------------------------------------
# Question 1: Multi-Step Arithmetic Operations
# -------------------------------------------

# Task:
# Use compound arithmetic operators to modify values of a, b, and c.
# Then calculate the square root of the sum of their squares.
# Tip: Use the math module.

import math

# Start with some base values
a = 5
b = 10
c = 7

# TODO: Add 3 to a using +=
# TODO: Multiply b by 2 using *=
# TODO: Modulo c by 4 using %=
a += 3
print("a =", a)
b *= 2
print("b =", b)
c %= 4
print("c =", c)
# TODO: Calculate the square root of (a^2 + b^2 + c^2)
(result) = math.sqrt(a**2 + b**2 + c**2)
print("result =", result)
# TODO: Print the final result rounded to 2 decimal places
print(f"final result = {result:.2f}")



# -------------------------------------------
# Question 2: Complex Conditional Evaluation
# -------------------------------------------

# Task:
# Ask the user to input three integers (x, y, z).
# Then evaluate and print whether:
# - x is even
# - y is positive
# - z is between 10 and 50
# Use logical operators to combine the conditions.

# Tip: Use and/or to join conditions.

# TODO: Input x, y, z
x = 5
print("x =", x)
y = 8
print("y =", y)
z = 11
print("z =", z)
# TODO: Create conditions:
#   is_even = True if x is even
if x % 2 == 0:
    is_even = True
else:
    is_even = False
print ("x is not even")
print (is_even)
    
    
#   is_positive = True if y > 0
if y > 0:
    is_positive = True
    print("y is positive")
    print(is_positive)
else:
    is_positive = False
#   is_in_range = True if z between 10 and 50
if 10 <= z <= 50:
    is_in_range = True
    print("z is in range") 
    print(is_in_range)
else:
    is_in_range = False
    print("z is not in range")
    print(is_in_range)
# TODO: Create final_condition = is_even and is_positive and is_in_range
final_condition = is_even and is_positive and is_in_range

# TODO: Print final_condition
print("final condition =", final_condition)

# -------------------------------------------
# Question 3: Grading with Adjustments
# -------------------------------------------

# Task:
# Ask the user for their base score, then apply:
# - bonus points (+5)
# - late penalty (-10)
# Final score must not exceed 100 or drop below 0.
# Then assign a grade.

# Tip: Use min() and max() to constrain the score.

# TODO: Input score from user
score = 85
# TODO: Apply adjustments
score += 5
score -= 10
# TODO: Clamp score between 0 and 100
score = max(0, min(100, score))
# TODO: Use if-elif-else to determine grade and print it
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B' 
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'
print("Grade:", grade)


# -------------------------------------------
# Question 4: Advanced Calculator
# -------------------------------------------

# Task:
# Ask the user to input two numbers and an operation (+, -, *, /, %, **).
# Handle division/modulus by zero with error checking.
# Perform the operation and print the result.

# Tip: Use try-except and elif branches for each operation.

# TODO: Input num1, num2
num1 = 10
num2 = 2
print("num1 =", num1)
print("num2 =", num2)
# TODO: Input operation
operation = "*"
print("operation =", operation)
# TODO: Match operation using if-elif
if operation == "+":
    result = num1 + num2
    print("num1 + num2 =", result)
elif operation == "-":
    result = num1 - num2
    print("num1 - num2 =", result)
elif operation == "*":
    result = num1 * num2
    print("num1 * num2 =", result)    
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print("num1 / num2 =", result)
    else:
        print("Error: Division by zero is not allowed.")
        result = None
elif operation == "%":
    if num2 != 0:
        result = num1 % num2
        print("num1 % num2 =", result)
    else:
        print("Error: Modulus by zero is not allowed.")
        result = None
elif operation == "**":
    result = num1 ** num2
    print("num1 ** num2 =", result)
else:
    print("Error: Invalid operation.")
    result = None

# TODO: Print result
print("Result:", result)

