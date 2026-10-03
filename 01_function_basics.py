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

    print("Marks:", marks)
    print("Grade:", grade)


check_grade(76)


# ======================================================
# TOPIC 3: FUNCTION WITH LOOP
# ======================================================

# ======================================================
# Q3. FIND HIGHEST MARKS
# ======================================================
# Create a function that finds the highest mark
# from a list without using max().

def find_highest(marks):

    # Start with the first mark as the highest.
     highest = marks[0]

     # Compare each mark with the current highest.
     for mark in marks:

        if mark > highest:
            highest = mark

     return highest

marks = [65, 88, 72, 91, 54]

highest = find_highest(marks)

print("Highest Marks:", highest)


# ======================================================
# TOPIC 4: FUNCTION WITH LIST
# ======================================================

# ======================================================
# Q4. COUNT PASSED STUDENTS
# ======================================================
# Create a function that counts how many students
# have marks of 50 or above.

def count_passed(marks):

    # Count students who have passed.
    passed = 0

    for mark in marks:

        if mark >= 50:
            passed += 1

    print("Passed Students:", passed)

marks = [45, 78, 62, 33, 91, 49, 70]
count_passed(marks)

# ======================================================
# TOPIC 5: FUNCTION WITH STRING
# ======================================================

# ======================================================
# Q5. PASSWORD STRENGTH CHECKER
# ======================================================
# Create a function that checks whether a password:
# - has at least 8 characters
# - contains a number
#
# Display Strong or Weak.

def check_password(password):

  # Check whether the password contains a number.
  has_number = False

  for character in password:
        if character.isdigit():
            has_number = True

  # Check the password length and number requirement.
  if len(password) >= 8 and has_number:
      print("Password: Strong")
  else:
      print("Password: Weak")

check_password("Python123")

# ======================================================
# TOPIC 6: FUNCTION WITH LIST AND LOOP
# ======================================================

# ======================================================
# Q6. FIND EVEN NUMBERS
# ======================================================
# Create a function that takes a list and displays
# all even numbers.

def display_even_numbers(numbers):

    print("Even Numbers:")