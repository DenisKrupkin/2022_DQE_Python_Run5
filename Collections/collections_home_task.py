"""
Home task for Module 2 - Collections

Write a code, which will:

1. create a list of random number of dicts (from 2 to 10)

dict's random numbers of keys should be letter,
dict's values should be a number (0-100),
example: [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]
2. get previously generated list of dicts and create one common dict:

if dicts have same key, we will take max value, and rename key with dict number with max value
if key is only in one dict - take it as is,
example: {'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}
Each line of code should be commented with description.

Commit script to git repository and provide link as home task result.
"""
import random
import string

# Create a list of random number of dicts (from 2 to 10)
list_of_random_dictionaries = []  # Define empty list of dictionaries
for _ in range(random.randint(2, 10)):  # FOR statement with randon number of iterations between 2 and 10
    sample_dictionary = {random.choice(string.ascii_lowercase): random.randint(0, 100)
                         for _ in range(random.randint(1, 100))}  # Generation of random dictionary
    list_of_random_dictionaries.append(sample_dictionary)  # Adding of generated dictionary to list
print(f'List of random dictionaries: {list_of_random_dictionaries}.')  # Printing of final list

# Get previously generated list of dicts and create one common dict
final_dict = {}  # Define empty final dictionary
common_dict = {}  # Define empty temporary dictionary
index = 0  # Default value for index of dictionaries in list
max_key = ''  # Default value for max_key in all dictionaries
try:  # Try for catch list index out of range error
    for dictionary in list_of_random_dictionaries:  # Take list of random dictionaries
        for key, value in dictionary.items():  # Take key and value of each item
            common_dict.update({f'{key}_{index}': value})  # Add key_index: value to common dictionary
        index += 1  # Increase index
except IndexError:  # Catch error
    print('Index error.')  # Print user friendly message
print(f'Common dictionary: {common_dict}')  # Print common dictionary

# Logic to find of max value for each letter and set number of dictionary in key
temp_dict = {}  # Define the empty temporary list
second_temp_dict = {}  # Define the empty temporary list
for letter in string.ascii_lowercase:  # For each letter in set_of_letters
    second_temp_dict.clear()  # Clear temporary dictionary
    temp_dict.clear()  # Clear temporary dictionary
    count_of_letters = 0  # Set default 0 to count_of_letter of found letters occurrences
    for key, value in common_dict.items():  # For each item in common dictionary
        if key[0] == letter:  # Compare the first letter in key with letter from set_of_letters set
            second_temp_dict.update({key: value})  # Add all found items to temporary list
            count_of_letters += 1  # Increase count_of_letter of occurrences of one letter
    if count_of_letters != 1 and count_of_letters != 0:  # If found letters number not 1 and not 0
        values_list = list(second_temp_dict.values())  # Create new list of values from temporary dict
        keys_list = list(second_temp_dict.keys())  # Create new list of keys from temporary dict
        try:  # Try for catch value error
            max_key = keys_list[values_list.index(max(values_list))]  # Calculate max of values in list
        except ValueError:
            print('Value error.')  # Print of user-friendly message
        temp_dict[max_key] = second_temp_dict[max_key]  # Adding of found max value to new temp dictionary
        final_dict.update(temp_dict)  # Adding of result to final dictionary
    elif count_of_letters == 1 and count_of_letters != 0:  # IF only one letter occurrence found
        values_list = list(second_temp_dict.values())  # Create new list of values from temporary dict
        keys_list = list(second_temp_dict.keys())  # Create new list of keys from temporary dict
        new_key = keys_list[0].partition('_')[0]  # Shrink 'a' key using partition. Delete all after first letter.
        temp_dict.update({new_key: values_list[0]})  # Adding of changed  key: value to new temp dictionary
        final_dict.update(temp_dict)  # Adding of result to final dictionary
print(f'Final dictionary:{final_dict}')  # Printing of final result to console.
