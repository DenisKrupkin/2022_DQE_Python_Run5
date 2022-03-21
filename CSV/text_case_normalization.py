class TextCaseNormalizer:
    @staticmethod
    def normalize_text_case(target_text, paragraph_splitter):
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
        target_text = f'. {paragraph_splitter}'.join(
            target_text_list)  # Create normalized final text with paragraphs
        return target_text  # Normalized text with correct letters case
