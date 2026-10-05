"""
========================================================
   LECTURE 06 - FILE 3: FUNCTION RETURN
========================================================
Topics: return values, print vs return, function return,
        recursion basics, and Python recursion
Total Questions: 10
========================================================
"""

# ======================================================
# TOPIC 1: BASIC RETURN VALUE
# ======================================================

# ======================================================
# Q1. CALCULATE TOTAL MARKS
# ======================================================
# Create a function that takes three subject marks
# and returns the total marks.

def calculate_total(math, python, english):

     # Calculate and return the total marks.
    total = math + python + english

    return total

total = calculate_total(75, 82, 68)

print("Total Marks:", total)
