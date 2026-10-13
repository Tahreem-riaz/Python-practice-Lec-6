"""
========================================================
       LECTURE 06 - FILE 4: RECURSION PRACTICE
========================================================
Topics: recursion, recursive functions, recursive
        problems, call stack, base case, recursive case,
        and factorial recursion
Total Questions: 8
========================================================
"""

# ======================================================
# TOPIC 1: BASIC RECURSION
# ======================================================

# ======================================================
# Q1. RECURSIVE COUNTDOWN
# ======================================================
# Create a recursive function that prints numbers
# from the given number down to 1.

def countdown(number):

# Stop the function when the number reaches 0.
    if number == 0:
        return

    print(number)

# Call the function with the next smaller number.
    countdown(number - 1)


countdown(7)

# ======================================================
# TOPIC 2: RECURSIVE FUNCTION
# ======================================================

# ======================================================
# Q2. SUM OF NUMBERS
# ======================================================
# Create a recursive function that calculates
# the sum of numbers from 1 to n.

def recursive_sum(number):

# Base case stops the recursion.
    if number == 0:
        return 0

# Add the current number to the recursive result.
    return number + recursive_sum(number - 1)

result = recursive_sum(5)

print("Sum:", result)


# ======================================================
# TOPIC 3: FACTORIAL RECURSION
# ======================================================

# ======================================================
# Q3. FACTORIAL CALCULATOR
# ======================================================
# Create a recursive function to calculate
# the factorial of a number.
#
# Example:
# 5! = 5 x 4 x 3 x 2 x 1

def factorial(number):

# Base case for factorial.
    if number == 1:
        return 1

# Multiply the number by the previous factorial.
    return number * factorial(number - 1)

result = factorial(5)

print("Factorial:", result)

# ======================================================
# TOPIC 4: RECURSIVE PROBLEM
# ======================================================

# ======================================================
# Q4. SUM OF DIGITS
# ======================================================
# Create a recursive function that calculates
# the sum of all digits of a number.

def sum_digits(number):

    # Base case for a single digit.
    if number == 0:
        return 0

   # Add the last digit and process the remaining digits.
    return number % 10 + sum_digits(number // 10)

result = sum_digits(452)

print("Sum of Digits:", result)

# ======================================================
# TOPIC 5: RECURSIVE STRING
# ======================================================

# ======================================================
# Q5. REVERSE A STRING
# ======================================================
# Create a recursive function that reverses
# a given string.

def reverse_string(text):

    # Base case when the string has one or no characters.
    if len(text) <= 1:
        return text
