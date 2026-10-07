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
