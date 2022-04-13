"""
Home task for Module 7 - CSV Parsing.
Calculate number of words and letters from previous Homeworks 5/6 output test file.
Create two csv:
1.word-count (all words are preprocessed in lowercase)
2.letter, count_all, count_uppercase, percentage (add header, space-characters are not included)
CSVs should be recreated each time new record added.
"""

import user_interface
import publications_parser
import publications
import csv_files_processor


def start():
    """
        Function for application starting.
        Function asks user to select publications input format and after according to choice loads or writes
        publications to target file.
        After publication finished asks user to choose "Yes" for continue or stop publishing answering "No".
        Catches exception if user answered something else except "Yes" or "No".
        """
    while True:
        parser = publications_parser.PublicationsParser()
        file_paths = parser.parse_files_paths()
        user_input = user_interface.UserInterface()
        input_format = user_input.ask_input_format()
        csv_processor = csv_files_processor.CsvProcessor()
        if input_format == '1':
            publication_type = user_input.ask_publication_type()
            if publication_type == '1':
                publications.News.publish_news(file_paths[1])
            elif publication_type == '2':
                publications.Advertisement.publish_advertisement(file_paths[1])
            elif publication_type == '3':
                publications.Article.publish_article(file_paths[1])
            else:
                print('Please enter a number between 1 and 3. Try again please.')
                continue
        elif input_format == '2':
            file_path_mode = user_input.ask_file_path_mode()
            if file_path_mode == '1':
                try:
                    parser.check_file_path(file_paths[0])
                    parser.check_file_path(file_paths[1])
                    parser.parse_target_file(file_paths[0], file_paths[1])
                except TypeError:
                    print('Default path is not set as parameter. '
                          'Set "--default_path <path to file>" parameter and try again.')
                except Exception:
                    print('Unknown error occurred. Check the --default_path parameter.')
            elif file_path_mode == '2':
                parser.check_file_path(file_paths[1])
                file_path = user_input.ask_file_path()
                parser.check_file_path(file_path)
                parser.parse_target_file(file_path, file_paths[1])
        user_choice = input('Do you want to add more publications? Type "Yes" or "No":\n')
        if user_choice == 'Yes':
            continue
        elif user_choice == 'No':
            csv_processor.create_statistics(file_paths[1], 'words_statistics.csv', 'letters_statistics.csv')
            break
        else:
            print('Incorrect value entered.')
            break


# Application starting
if __name__ == '__main__':
    start()
