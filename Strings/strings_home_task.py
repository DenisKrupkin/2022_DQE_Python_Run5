"""
Home task for Module 3 - Strings

"""

# Creation of variable as required at home task
corrupted_text = """homEwork:

  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

# Cleaning of text and adding it to the one list
formatted_text = []  # Create an empty list for formatted text
PARAGRAPH_SPLITTER = '\n\n\n\n'
for paragraph in corrupted_text.split('.\n'):  # Split paragraphs by \n\n\n\n
    temporary_list_for_paragraph = []  # Initialize separate list for one paragraph for further operations
    temporary_string_for_paragraph = ''  # Initialize temporary string for one paragraph
    for sentences in paragraph.split('.'):  # Split sentences inside of paragraph by '.'
        sentences = sentences.strip().lower().replace(' iz ', ' is ').capitalize()  # Polish the sentence, fix " iz "
        temporary_list_for_paragraph.append(sentences)  # Adding to temp list
        temporary_string_for_paragraph = '. '.join(temporary_list_for_paragraph)  # Joint to temp string
    formatted_text.append(temporary_string_for_paragraph + f'. {PARAGRAPH_SPLITTER}')  # Adding to final result

# Generation of sentence from the latest words in each paragraph
list_for_sentence = []  # Initialize of new list for sentence building
string_for_sentence_building = (''.join(formatted_text))  # Populate temporary string with all words from formatted text
for _ in string_for_sentence_building.split(f' {PARAGRAPH_SPLITTER}'):  # Split with removing whitespaces
    list_for_sentence = [
        word for word in string_for_sentence_building.split(' ') if word.endswith('.')]  # Making raw sentence in list
final_sentence = ' '.join(list_for_sentence).replace('.', '').capitalize().strip()  # Polish and add to result string

# Adding generated sentence to the list with cleaned text
formatted_text[1] = \
    formatted_text[1].replace(f'. {PARAGRAPH_SPLITTER}', '. ') + final_sentence + f'. {PARAGRAPH_SPLITTER}'

# Finalizing of text
corrected_text = ''  # # Initialize of empty string for corrected text
for _ in formatted_text:
    corrected_text = ' '.join(formatted_text)  # Adding list values to string
corrected_text = corrected_text.removesuffix(f' . {PARAGRAPH_SPLITTER}')  # Removing of '. \n\n\n\n' at the end
print(f'Corrected_text : {corrected_text}')  # Printing of corrected text

# Count of whitespaces
count_of_whitespaces = corrected_text.count(' ') + corrected_text.count('\n')  # Calculation of whitespaces via count
print(f'Count of whitespaces: {count_of_whitespaces}')
