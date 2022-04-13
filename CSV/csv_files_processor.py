import csv
import string
import os


class CsvProcessor:
    @staticmethod
    def count_words(source_file_path, target_csv_file_path):
        """
        Method calculates count of each separate word in source text in target csv file.
        CSV file rewrites each time after last execution.
        @param source_file_path: path to source text
        @param target_csv_file_path: path to result csv file
        """
        result = {}
        with open(f'{source_file_path}', 'r') as source_file:
            text = source_file.read().lower()
            for symbol in string.punctuation:
                text = text.replace(symbol, ' ')
            text_list = [word for word in text.replace('\n', ' ').split(' ') if word.isalpha()]
            for word in text_list:
                count = ' '.join(text_list).count(word)
                result.update({word: count})
        with open(f'{target_csv_file_path}', 'w', newline='') as target_csv:
            writer = csv.writer(target_csv)
            for word, count in result.items():
                writer.writerow([word, count])

    @staticmethod
    def count_all_letter(letter, source_file_path):
        """
        Method calculates count of specified letter in text
        @param letter: letter for count calculation
        @param source_file_path: path to file with source text
        @return: count of letter
        """
        with open(f'{source_file_path}', 'r') as source_file:
            text = source_file.read()
            count = text.count(letter.lower()) + text.count(letter.upper())
            return count

    @staticmethod
    def count_upper_letter(letter, source_file_path):
        """
        Method calculates count of specified letter in upper case.
        @param letter: letter for uppercase count calculation
        @param source_file_path: path to file with source text
        @return: count of uppercase
        """
        with open(f'{source_file_path}', 'r') as source_file:
            text = source_file.read()
            count = text.count(letter.upper())
            return count

    @staticmethod
    def calculate_letter_percentage(letter, source_file_path):
        """
        Method calculates specified letter percentage in the source text.
        @param letter: letter for percentage calculation
        @param source_file_path: path to file with source text
        @return: percentage for letter
        """
        with open(f'{source_file_path}', 'r') as source_file:
            text = source_file.read().lower()
            letter_count = text.count(letter)
            all_letters_count = 0
            for symbol in string.ascii_lowercase:
                for text_symbol in text:
                    if symbol == text_symbol:
                        all_letters_count += 1
            letter_percentage = round((letter_count * 100) / all_letters_count, 2)
        return letter_percentage

    @staticmethod
    def write_letters_statistics(source_file_path, target_csv_file_path):
        """
        Method that takes path to file with some text and calculate letters statistics
        for each letter in string.ascii.lowercase.
        Statistic is letter - letter total count - letter count in upper case - letter percentage.
        Calculated statistics writes to target csv file.
        CSV file rewrites each time after last execution.
        @param source_file_path: path to source file with text
        @param target_csv_file_path: path to result csv file.
        """
        with open(f'{target_csv_file_path}', 'w', newline='') as target_csv:
            parser = CsvProcessor()
            headers = ['letter', 'letter_total', 'letter_upper_total', 'letter_percentage']
            writer = csv.DictWriter(target_csv, fieldnames=headers)
            writer.writeheader()
            for letter in string.ascii_lowercase:
                total_letter = parser.count_all_letter(letter, source_file_path)
                total_letter_upper = parser.count_upper_letter(letter, source_file_path)
                letter_percentage = parser.calculate_letter_percentage(letter, source_file_path)
                writer.writerow({'letter': letter,
                                 'letter_total': total_letter,
                                 'letter_upper_total': total_letter_upper,
                                 'letter_percentage': letter_percentage})

    @staticmethod
    def create_statistics(source_file_path, target_words_csv_file_path, target_letters_csv_file_path):
        """
        Method creates full statistics for words and letters published in target file.
        @param source_file_path: Path to file with publications
        @param target_words_csv_file_path: Path to file with words statistics
        @param target_letters_csv_file_path: Path to file with letters statistics
        """
        text_parser = CsvProcessor
        text_parser.count_words(source_file_path, target_words_csv_file_path)
        text_parser.write_letters_statistics(source_file_path, target_letters_csv_file_path)
        print(f'Statistics created. Find statistics csv files in working directory: '
              f'{os.path.dirname(os.path.abspath(__file__))}.')
