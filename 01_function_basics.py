"""
========================================================
       LECTURE 06 - FILE 1: FUNCTION BASICS
========================================================
Topics: creating functions, function calls,
        conditions, loops, lists, and strings
Total Questions: 10
========================================================
"""

# ======================================================
# TOPIC 1: FUNCTION WITH CALCULATION
# ======================================================

# ======================================================
# Q1. CALCULATE SHOPPING BILL
# ======================================================
# Create a function that takes item prices,
# calculates the total, and applies a discount
# if the total is greater than 2000.

def calculate_bill(prices):

    # Calculate the total price.
    total = 0

    for price in prices:
        total += price

   # Apply a 10% discount if the total is above 2000.
    if total > 2000:
        discount = total * 0.10
        total = total - discount
        print("10% Discount Applied")

    print("Final Bill:", total)

prices = [450, 700, 350, 600]

calculate_bill(prices)

# ======================================================
# TOPIC 2: FUNCTION WITH CONDITIONS
# ======================================================

# ======================================================
# Q2. STUDENT GRADE CHECKER
# ======================================================
# Create a function that takes marks and displays
# the grade according to the following:
#
# 80 or above -> A
# 70 or above -> B
# 60 or above -> C
# 50 or above -> D
# Below 50 -> F

def check_grade(marks):

# Determine the grade according to the marks.
    if marks >= 80:
        grade = "A"

    elif marks >= 70:
        grade = "B"

    elif marks >= 60:
        grade = "C"

    elif marks >= 50:
        grade = "D"

    else:
        grade = "F"