"""
Home task for Module 1 - Python Basics

Create a python script:
create list of 100 random numbers from 0 to 1000
sort list from min to max (without using sort())
calculate average for even and odd numbers
print both average result in console
"""
import random  # Import of random module for using of random function
import statistics  # Import of statistics module for using mean() function

# Create list of 100 random numbers from 0 to 1000
random_numbers = [random.randint(0, 999) for j in range(1000)]  # Creation of list with random numbers via comprehension
print(f'List with generated random values: {random_numbers}.')  # Printing final list to console

# Sort list from min to max (without using sort())
for run in range(len(random_numbers)-1):  # Define of initial FOR statement with range of iterations minus 1 from list
    for i in range(len(random_numbers)-1-run):  # Inner FOR statement with decreasing iterations for each run
        if random_numbers[i] > random_numbers[i+1]:  # Compare two adjacent values from list
            random_numbers[i], random_numbers[i+1] = random_numbers[i+1], random_numbers[i]  # Swap places
print(f'Sorted from min to max list: {random_numbers}.')  # Printing of sorted by bubble sorting list

# Calculate average for even and odd numbers
even_numbers = [number for number in random_numbers if number % 2 == 0]  # Creation of list with even numbers
odd_numbers = [number for number in random_numbers if number % 2 != 0]  # Creation of list with odd numbers
even_average = statistics.mean(even_numbers)  # Calculation of mean value for even numbers via mean()
odd_average = statistics.mean(odd_numbers)  # Calculation of mean value for odd numbers via mean()

# Print both average result in console
print(f'Average count of even numbers: {even_average}.')  # Printing of average of even numbers to console
print(f'Average count of odd numbers: {odd_average}.')  # Printing of average of odd numbers to console
