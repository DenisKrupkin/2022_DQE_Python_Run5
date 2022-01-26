"""
Home task for Module 1 - Python Basics

Create a python script:
create list of 100 random numbers from 0 to 1000
sort list from min to max (without using sort())
calculate average for even and odd numbers
print both average result in console
"""
import random  # Import of random module for using of random function

list_of_random = []  # Define the empty list
for j in range(1000):  # Define of FOR statement with range of iterations from 0 to 999
    list_of_random.append(random.randint(0, 999))  # Adding of randomly generated by randint function INT values to list
print('List with generated random values:', list_of_random)  # Printing final list to console
# Sort list from min to max (without using sort())
for run in range(len(list_of_random) - 1):  # Define of initial FOR statement with range of iterations minus 1 from list
    for i in range(len(list_of_random) - 1 - run):  # Inner FOR statement with decreasing iterations for each run
        if list_of_random[i] > list_of_random[i + 1]:  # Compare two adjacent values from list
            list_of_random[i], list_of_random[i + 1] = list_of_random[i + 1], list_of_random[i]  # Swap places
print('Sorted from min to max list:', list_of_random)  # Printing of sorted by bubble sorting list
# Calculate average for even and odd numbers
even_numbers = []  # Define empty list for even numbers
odd_numbers = []  # Define empty list for odd numbers
for i in range(len(list_of_random)):  # Define FOR statement with number of iterations equal to list length
    if list_of_random[i] % 2 == 0:  # Check if number can be divided by 2 without reminder
        even_numbers.append(list_of_random[i])  # Adding of even values to separate list
    else:
        odd_numbers.append(list_of_random[i])  # Else other values added to odd values list
for i in range(len(even_numbers)):  # Define of FOR statement with range equal to even numbers list length
    total = 0  # Define of variable for calculation of total with 0 value
    total = total + even_numbers[i]  # Calculation of total sum
try:  # Zero division error handling
    even_average = total / len(even_numbers)  # Calculation of average even number
except ZeroDivisionError:  # In case of zero division error
    print('Zero division error.')  # Printing message
for i in range(len(odd_numbers)):  # Define of FOR statement with range equal to odd numbers list length
    total = 0  # Clearing of total with 0 value
    total = total + odd_numbers[i]  # Calculation of total sum
try:  # Zero division error handling
    odd_average = total / len(odd_numbers)  # Calculation of average odd number
except ZeroDivisionError:  # In case of zero division error
    print('Zero division error.')  # Printing message
print('Average count of even numbers:', even_average)  # Printing of average of even numbers to console
print('Average count of odd numbers:', odd_average)  # Printing of average of odd numbers to console
