"""
Home task for Module 4 - Functions (based on home task for Strings module)
"""


def fix_misspellings(misspell, correct_text, target_string):
    """
    Function to fix specified misspell in specified text.
    @param misspell: misspell to fix
    @param correct_text: correct variant of text
    @param target_string: string to fix misspell
    @return: string with corrected misspell
    """
    return target_string.replace(f'{misspell}', f'{correct_text}')


def normalize_paragraphs_letters_case(target_text, paragraph_splitter):
    """
    Function generates text with normalized letters case from target_text and paragraphs structure.
    @param target_text: text to normalize
    @param paragraph_splitter: paragraph splitter for target text
    @return: text with corrected letters case and paragraphs
    """
    # Split text by sentences and without whitespaces at the beginning and the capitalizes it:
    target_text = '. '.join(item.lstrip().capitalize() for item in target_text.split('. '))
    target_text_list = []  # Create list for store normalized sentences
    for sentence in target_text.split('.\n'):  # Split text by paragraphs
        sentence = sentence.strip()  # Delete whitespaces
        sentence = sentence[0].capitalize() + sentence[1:]  # Make first letter in sentence capitalized
        target_text_list.append(sentence)  # Add normalized sentence to list
    target_text = f'. {paragraph_splitter}'.join(target_text_list)  # Create normalized final text with paragraphs
    return target_text  # Normalized text with correct letters case


def generate_last_paragraph_words_sentence(target_text, paragraph_splitter):
    """
    Function generates sentence from last words of each sentence in text with handling of paragraphs.
    @param target_text: text with sentences
    @param paragraph_splitter: paragraphs splitter for handling
    @return: sentence from last words of all sentences
    """
    for _ in target_text.split(f' {paragraph_splitter}'):  # Split with removing whitespaces
        sentence_list = [
            word for word in target_text.split(' ') if word.endswith('.')]  # Create list with words ends with '. '
    result_sentence = ' '.join(sentence_list).replace('.', '').capitalize().strip()  # Generate sentence
    return result_sentence


def add_specified_sentence(sentence, paragraph_number, target_text, paragraph_splitter):
    """
    Function adds sentence to specified paragraph in text and save paragraphs structure.
    @param sentence: sentence for adding
    @param paragraph_number: number of paragraph to add sentence
    @param target_text: text with paragraphs
    @param paragraph_splitter: paragraphs splitter for storing paragraphs structure
    @return: result text with sentence
    """
    target_text_list = target_text.split(f'{paragraph_splitter}')  # Split text by paragraphs
    target_text_list[paragraph_number] = \
        target_text_list[paragraph_number].replace(f'. {paragraph_splitter}', '. ') + f'{sentence}' + f'.'
    target_text = f'{paragraph_splitter}'.join(target_text_list)  # Adding sentence with paragraph splitter at the end
    return target_text


def calculate_whitespaces(target_text, *whitespaces):
    """
    Function calculates count of specified whitespaces in target text.
    @param target_text: text for whitespaces calculation
    @param whitespaces: tuple with set of whitespaces
    @return: total count of all specified whitespaces
    """
    count_whitespaces = 0
    for whitespace in whitespaces:
        if whitespace in target_text:
            count_whitespaces += target_text.count(whitespace)
    return count_whitespaces


# Global variable to store the text paragraph splitter
PARAGRAPH_SPLITTER = '\n\n\n\n'
# Creation of variable as required at home task.
corrupted_text = """homEwork:

  tHis iz your homeWork, copy these Text to variable.

 

  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

 

  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

 

  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

# Generate normalized text from variable.
normalized_text = normalize_paragraphs_letters_case(corrupted_text, PARAGRAPH_SPLITTER)

# Generate sentence from last words of all sentences.
generated_sentence = (generate_last_paragraph_words_sentence(normalized_text, PARAGRAPH_SPLITTER))

# Add sentence to target paragraph in text.
normalized_text_sentence = add_specified_sentence(generated_sentence, 1, normalized_text, PARAGRAPH_SPLITTER)

# Fix specified misspellings in text.
normalized_text_sentence_fixed_misspell = fix_misspellings(' iz ', ' is ', normalized_text_sentence)

# Calculation count of whitespaces in text.
whitespaces_count = calculate_whitespaces(normalized_text_sentence_fixed_misspell, ' ', '\n', '\t')


# Printing of completely normalized text.
print(normalized_text_sentence_fixed_misspell)

# Printing count of whitespaces.
print(f'Count of whitespaces: {whitespaces_count}')
