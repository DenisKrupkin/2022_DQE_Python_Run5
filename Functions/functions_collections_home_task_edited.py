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


def generate_random_keys_values_dict(keys, min_value, max_value, min_count, max_count):
    """
    Function generates a dictionary with defined ranges of random keys and values.
    @param keys: possible keys set
    @param min_value: min possible number for value
    @param max_value: max possible number for value
    @param min_count: min count of values to generate
    @param max_count: max count of values to generate
    @return: random key to random value dict with random count of {key: value} pairs
    """
    return {random.choice(keys): random.randint(min_value, max_value) for _ in
            range(random.randint(min_count, max_count))}


def create_random_dictionaries_list(min_dicts_count, max_dicts_count,
                                    keys,
                                    min_value, max_value,
                                    min_values_count, max_values_count):
    """
    Function generates list with random count of dictionaries with random set of keys and values.
    @param min_dicts_count: min possible count of dictionaries
    @param max_dicts_count: max possible count of dictionaries
    @param keys: possible keys set
    @param min_value: min possible value in dictionaries
    @param max_value: max possible value in dictionaries
    @param min_values_count: min possible count of keys and values in dictionaries
    @param max_values_count: min possible count of keys and values in dictionaries
    @return: random count of dicts with random count of pairs {key: value} in one list
    """
    return [generate_random_keys_values_dict(keys, min_value, max_value, min_values_count, max_values_count)
            for _ in
            range(random.randint(min_dicts_count, max_dicts_count))]


def generate_all_keys_dictionary(random_dictionaries_list):
    """
    Function takes list with random dictionaries and generates one dictionary with all keys and values
    with adding number of dictionary to each key.
    @param random_dictionaries_list: list with random count of dictionaries with randon keys and values
    @return: dictionary with all keys and values in form: {key_number: value}
    """
    all_keys_values_dictionary = {}  # Define empty temporary dictionary
    index = 0  # Define default index
    for dictionary in random_dictionaries_list:  # Take list of random dictionaries
        for letter, number in dictionary.items():  # Take key and value of each item
            all_keys_values_dictionary.update({f'{letter}_{index}': number})  # Add key_index: value to dictionary
        index += 1  # Increase index
    return all_keys_values_dictionary  # Return dictionary


def find_maximum_dictionary_key_value(set_of_keys_in_dict, dictionary):
    """
    Function to find the max value for each single key in dict and put it to separate dict.
    @param set_of_keys_in_dict: set of possible keys used in dictionary
    @param dictionary: dictionary with all keys and values with added indexes in key name
    @return: dictionary with maximum value for each unique key with number of parent dictionary in key name.
    Adds key without number of dictionary in case if key appears only one time in all dictionaries.
    """
    result_dict = {}  # Create final empty dictionary
    for key_symbol in set_of_keys_in_dict:  # For defined set of possible key values
        same_symbol_dict = {}  # Create dictionary for store all values for separate symbol
        for _, combination in enumerate(dictionary.items()):  # For all combinations of key: value
            if combination[0][0] == key_symbol:  # Compare first symbol in key with current letter, if matches:
                dict_key, dict_value = combination  # Separate tuple to separate key and value
                same_symbol_dict.update({dict_key: dict_value})  # Add new pair to dictionary
        if len(same_symbol_dict) > 1:  # Check if length of temp dictionary more than 1
            max_key = max(same_symbol_dict, key=same_symbol_dict.get)  # Find key with max value
            result_dict.update({max_key: same_symbol_dict[max_key]})  # Add to final dictionary
        elif len(same_symbol_dict) == 1:  # If length of temporary dictionary equal to one
            updated_key = dict_key[0]  # Take only first letter of key
            result_dict.update({updated_key: same_symbol_dict[dict_key]})  # Add changed key: value to final dict
    return result_dict  # Return final dictionary


# Generate list with random dicts
random_dicts_list = create_random_dictionaries_list(2, 10, string.ascii_lowercase, 0, 100, 1, 100)
print(f'List with random dicts: {random_dicts_list}')

# Generate common dictionary:
all_keys_dictionary = generate_all_keys_dictionary(random_dicts_list)

# Generate final dictionary with result
result_dictionary = find_maximum_dictionary_key_value(string.ascii_lowercase, all_keys_dictionary)
print(f'Result dictionary: {result_dictionary}')
