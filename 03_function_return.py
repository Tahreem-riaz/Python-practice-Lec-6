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

def analyze_numbers(numbers):

     # Calculate the required values.
    total = sum(numbers)
    highest = max(numbers)
    lowest = min(numbers)

    return total, highest, lowest

numbers = [12, 45, 8, 67, 23]

total, highest, lowest = analyze_numbers(numbers)

print("Total:", total)
print("Highest:", highest)
print("Lowest:", lowest)

# ======================================================
# TOPIC 5: RETURN WITH STRING
# ======================================================

# ======================================================
# Q5. CREATE USERNAME
# ======================================================
# Create a function that takes first name and roll number
# and returns a formatted username.
#
# Example:
# Ali + 25 -> ali_25

def create_username(name, roll_number):

    # Create and return the formatted username.
    username = name.lower() + "_" + str(roll_number)

    return username

username = create_username("Ali", 25)

print("Username:", username)

# ======================================================
# TOPIC 6: RETURN WITH CALCULATION
# ======================================================

# ======================================================
# Q6. CALCULATE FINAL PRICE
# ======================================================
# Create a function that takes price and discount.
# Return the final price after applying the discount.

def calculate_final_price(price, discount):

    # Calculate the discount and final price.
    discount_amount = price * discount / 100
    final_price = price - discount_amount

    return final_price

final_price = calculate_final_price(2500, 15)

print("Final Price:", final_price)

# ======================================================
# TOPIC 7: FUNCTION RETURN WITH SEARCH
# ======================================================

# ======================================================
# Q7. SEARCH FOR AN ITEM
# ======================================================
# Create a function that searches for an item
# in a list and returns True or False.

def search_item(items, search):

    # Return True when the item is found.
    for item in items:

        if item.lower() == search.lower():
            return True

    return False

items = ["Python", "C++", "Database", "HTML"]

found = search_item(items, "Python")

print("Item Found:", found)


# ======================================================
# TOPIC 8: RECURSION BASICS
# ======================================================

# ======================================================
# Q8. COUNT DOWN USING RECURSION
# ======================================================
# Create a recursive function that prints numbers
# from the given number down to 1.

def countdown(number):

     # Stop the recursion when the number reaches 0.
    if number == 0:
        return

    print(number)

    countdown(number - 1)


countdown(5)