"""
========================================================
     LECTURE 06 - FILE 2: FUNCTION PARAMETERS
========================================================
Topics: parameters, arguments, multiple parameters,
        default parameters, and practical functions
Total Questions: 10
========================================================
"""

# ======================================================
# TOPIC 1: MULTIPLE PARAMETERS
# ======================================================

# ======================================================
# Q1. CALCULATE STUDENT AVERAGE
# ======================================================
# Create a function that takes three subject marks
# and calculates the average.

def calculate_average(math, python, english):

     # Calculate the total marks and average.
    total = math + python + english
    average = total / 3

    print("Total:", total)
    print("Average:", average)

calculate_average(75, 82, 68)

# ======================================================
# TOPIC 2: PARAMETERS WITH CONDITIONS
# ======================================================

# ======================================================
# Q2. CHECK ELIGIBILITY
# ======================================================
# A student is eligible if:
# - age is 18 or above
# - marks are 50 or above

def check_eligibility(age, marks):

     # Check the age and marks requirements.
    if age >= 18 and marks >= 50:
        print("Student is Eligible")
    else:
        print("Student is Not Eligible")

check_eligibility(19, 72)

# ======================================================
# TOPIC 3: STRING PARAMETERS
# ======================================================

# ======================================================
# Q3. USERNAME VALIDATOR
# ======================================================
# Create a function that checks a username.
#
# Conditions:
# - minimum 5 characters
# - maximum 15 characters
# - no spaces

def validate_username(username):

    if len(username) < 5:
        print("Username is too short")

    elif len(username) > 15:
        print("Username is too long")

    elif " " in username:
        print("Username cannot contain spaces")

    else:
        print("Username is valid")

validate_username("student123")


# ======================================================
# TOPIC 4: LIST PARAMETER
# ======================================================
