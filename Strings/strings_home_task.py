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
formatted_text = []  # Creatre an empty list for formatted text
for paragraph in corrupted_text.split('.\n\n\n\n  '):  # Split paragraphs by \n\n\n\n
    temporary_list_for_paragraph = []  # Initialize separate list for one paragraph for further operations
    temporary_string_for_paragraph = ''  # Initialize temporary string for one paragraph
    for sentences in paragraph.split('.'):  # Split sentences inside of paragraph by '.'
        sentences = sentences.strip().lower().replace(' iz ', ' is ').capitalize()  # Polish the sentence, fix " iz "
        temporary_list_for_paragraph.append(sentences)  # Adding to temp list
        temporary_string_for_paragraph = '. '.join(temporary_list_for_paragraph)  # Joint to temp string
    formatted_text.append(temporary_string_for_paragraph + '. \n\n\n\n')  # Adding to final result with line breaks

# Generation of sentence from the latest words in each paragraph
list_for_sentence = []  # Initialize of new list for sentence building
final_sentence = ''  # Initialize of empty string for final sentence
string_for_sentence_building = (''.join(formatted_text))  # Populate temporary string with all words from formatted text
for _ in string_for_sentence_building.split(' \n\n\n\n'):  # Split with removing whitespaces
    list_for_sentence = [
        word for word in string_for_sentence_building.split(' ') if word.endswith('.')]  # Making raw sentence in list
final_sentence = ' '.join(list_for_sentence).replace('.', '').capitalize().strip()  # Polish and add to result string

# Adding generated sentence to the list with cleaned text
formatted_text[1] = formatted_text[1].replace('. \n\n\n\n', '. ') + final_sentence + '. \n\n\n\n'

# Finalizing of text
corrected_text = ''  # # Initialize of empty string for corrected text
for _ in formatted_text:
    corrected_text = ' '.join(formatted_text)  # Adding list values to string
corrected_text = corrected_text.removesuffix(' . \n\n\n\n')  # Removing of '. \n\n\n\n' at the end of final string
print(f'Corrected_text : {corrected_text}')  # Printing of corrected text

# Count of whitespaces
count_of_whitespaces = corrected_text.count(' ') + corrected_text.count('\n')  # Calculation of whitespaces via count
print(f'Count of whitespaces: {count_of_whitespaces}')
