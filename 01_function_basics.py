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

