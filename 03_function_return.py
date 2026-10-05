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

# ======================================================
# TOPIC 2: RETURN VS PRINT
# ======================================================

# ======================================================
# Q2. CALCULATE AVERAGE
# ======================================================
# Create a function that calculates the average
# and returns the result.
#
# Use the returned value outside the function.

def calculate_average(marks):

        # Calculate the average and return it.
    total = sum(marks)
    average = total / len(marks)

    return average

marks = [75, 82, 68, 91]

average = calculate_average(marks)

print("Average:", average)

# ======================================================
# TOPIC 3: RETURN WITH CONDITIONS
# ======================================================

# ======================================================
# Q3. CHECK PASS OR FAIL
# ======================================================
# Create a function that takes marks and returns:
# "Pass" if marks are 50 or above
# "Fail" if marks are below 50

def check_result(marks):

    # Return the result according to the marks.
    if marks >= 50:
        return "Pass"
    else:
        return "Fail"

result = check_result(72)

print("Result:", result)

# ======================================================
# TOPIC 4: RETURN MULTIPLE VALUES
# ======================================================

# ======================================================
# Q4. ANALYZE NUMBERS
# ======================================================
# Create a function that takes a list of numbers
# and returns the total, highest, and lowest value.