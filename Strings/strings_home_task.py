"""
Home task for Module 3 - Strings

"""
import re

# Creation of variable as required at home task
home_task_variable = """homEwork:

  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

# Preparations to formatting
home_task_variable_list = [item for item in home_task_variable]  # Creation of temporary list
temp_string_variable = home_task_variable.split('\n  ')  # Split of string variable to one dict
strings_dict = {}

# Replace "IZ" with "is" and make sentences lowercase and Capitalize
for_is = ' is '  # Temporary variable for store 'is'
for index, item in enumerate(temp_string_variable):  # Enumerate through dictionary
    strings_dict[index] = item  # Create mapping
    for key, value in strings_dict.items():
        strings_dict[key] = strings_dict[key].lower()  # Make all symbols lowercase
        strings_dict[key] = re.sub(r' iz ', for_is, strings_dict[key])  # Replace "iz" with 'is'
        strings_dict[key] = strings_dict[key].capitalize()  # Capitalize first letters in each value
for key, value in strings_dict.items():  # Attempt to capitalize inner sentences in each value
    number_of_dot = value.find('. ')  # Find one occurrence of '. ' in each value
    if number_of_dot != -1:  # If found then capitalize by indexes
        value = value[:number_of_dot] + '. ' + value[number_of_dot + 2].capitalize() + value[number_of_dot + 3:]
        strings_dict[key] = value  # Replace value with capitalized

# Adding of new sentence to 2 paragraph
sentence = ''  # Empty variable for sentence
temp_string = ''  # Empty temp string variable
for key, value in strings_dict.items():  # For each value in dictionary
    value = value.replace('\n', '')  # Replace \n with nothing
    temp_string += "".join(value)  # Split all words to one temp string
sentence += ' '.join(re.findall(r'[a-zA-Z0-9_]+\.', temp_string))  # Find all word that ends with '.'
sentence = (sentence.replace('.', '') + ".").capitalize()  # Create one sentence with formatting
strings_dict[2] = strings_dict[2].replace('\n', '')  # Temporary removing of \n
strings_dict[2] = strings_dict[2] + ' ' + sentence + '\n\n'  # Adding sentence and \n\n after it for restore initial

# Creation of final string
formatted_string = ''  # Variable for final string
for key, value in strings_dict.items():
    formatted_string += value + '\n\n '  # Adding \n\n removed before
formatted_string = formatted_string.replace(' i got 87.', ' I got 87.')  # Hard code to capitalize one last sentence
print(formatted_string)  # Printing of final string

# Count of whitespaces
set_of_whitespaces = ('\n', '\t', ' ', '\r', '\f', '\v')  # Creation of tuple with whitespaces
count_of_whitespaces = 0  # Initialize variable for count of whitespaces
for symbol in home_task_variable:  # For each symbol in initial string
    if symbol in set_of_whitespaces:  # If symbol exists in list
        count_of_whitespaces += 1  # Increase number of whitespaces
print(f'Count of whitespaces: {count_of_whitespaces}')  # Print number of whitespaces
