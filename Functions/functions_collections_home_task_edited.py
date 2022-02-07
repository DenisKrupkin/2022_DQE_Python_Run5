"""
Home task for Module 4 - Functions (Based on Module 2 - Collections home task)

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


# Function for generation of single dictionary with defined ranges of random keys and values
def generate_dictionary_with_random_keys_and_values(
        set_of_keys,
        start_of_value, end_of_value,
        start_of_total_count, end_of_total_count,
):
    final_dictionary = {random.choice(set_of_keys): random.randint(start_of_value, end_of_value)
                        for _ in range(random.randint(start_of_total_count, end_of_total_count))}
    return final_dictionary


# Function for generation of list with defined count of random generated dictionaries
def create_list_with_random_dictionaries(start_of_count_of_dicts, end_of_count_of_dicts):
    list_of_random_dicts = []
    for _ in range(random.randint(start_of_count_of_dicts, end_of_count_of_dicts)):
        list_of_random_dicts.append(
            generate_dictionary_with_random_keys_and_values(string.ascii_lowercase, 0, 100, 1, 100))
    return list_of_random_dicts


# Function for generation of one dictionary with all keys and values in one place
def create_common_dictionary_with_letter_indexes_in_keys(list_with_dictionaries):
    common_dictionary = {}  # Define empty temporary dictionary
    index = 0  # Define default index
    for dictionary in list_with_dictionaries:  # Take list of random dictionaries
        for letter, number in dictionary.items():  # Take key and value of each item
            common_dictionary.update({f'{letter}_{index}': number})  # Add key_index: value to common dictionary
        index += 1  # Increase index
    return common_dictionary  # Return dictionary


# Function to find the max value for each letter in dict and put it to separate dict
def find_maximum_value_and_put_into_dictionary(set_of_keys, dictionary):
    final_last_dict = {}  # Create final empty dictionary
    for letter in set_of_keys:  # For defined set of possible key values
        temp_letter_dict = {}  # Create temporary dictionary
        for _, combination in enumerate(dictionary.items()):  # For all combinations of key: value
            if combination[0][0] == letter:  # Compare first letter in key with current letter, if matches:
                dict_key, dict_value = combination  # Separate tuple to separate key and value
                temp_letter_dict.update({dict_key: dict_value})  # Add new pair to dictionary
        if len(temp_letter_dict) > 1:  # Check if length of temp dictionary more than 1
            max_key = max(temp_letter_dict, key=temp_letter_dict.get)  # Find key with max value
            final_last_dict.update({max_key: temp_letter_dict[max_key]})  # Add to final dictionary
        elif len(temp_letter_dict) == 1:  # If length of temporary dictionary equal to one
            updated_key = dict_key[0]  # Take only first letter of key
            final_last_dict.update({updated_key: temp_letter_dict[dict_key]})  # Add changed key: value to final dict
    return final_last_dict  # Return final dictionary


list_of_random_dictionaries = create_list_with_random_dictionaries(2, 10)  # Generate list with dicts
print(f'List with random dicts: {list_of_random_dictionaries}')

# Generate common dictionary:
result_dictionary = create_common_dictionary_with_letter_indexes_in_keys(list_of_random_dictionaries)

# Generate final dictionary with result
final_result_dictionary = find_maximum_value_and_put_into_dictionary(string.ascii_lowercase, result_dictionary)
print(f'Final result dictionary: {final_result_dictionary}')
