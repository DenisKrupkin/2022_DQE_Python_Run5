"""
Home task for Module 6 - Module. Files.
Expand previous Homework 5 with additional class, which allow providing records by text file:
1.Define your input format (one or many records)
2.Default folder or user provided file path
3.Remove file if it was successfully processed
4.Apply case normalization functionality form Homework 3/4
"""

import datetime
import text_case_normalization
import user_interface
import publications
import publications_parser


def publish_news(file_path):
    """
        Function for publishing of news scenario.
        Function creates objects of UserInterface, News classes.
        Asks user to enter publication text, city.
        After writes entered data to file.
        Catches exception if target file not found.
    """
    try:
        publications_parser.PublicationsParser.check_file_path(file_path)
        user_input = user_interface.UserInterface()
        publication_text = user_input.ask_publication_text()
        publication_text = text_case_normalization.normalize_text_case(publication_text, '')
        city = user_input.ask_city()
        publication_date = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        publications.News.write_news(city, publication_date, publication_text, file_path)
        print('The publication was published successfully.')
    except FileNotFoundError:
        print("Target file not found. Please check News_file.txt")


def publish_advertisement(file_path):
    """
        Function for publishing of advertisement scenario.
        Function creates objects of UserInterface, Advertisement classes.
        Asks user to enter publication text, expiration date.
        After writes entered data to file.
        Catches exception if target file not found.
    """
    try:
        publications_parser.PublicationsParser.check_file_path(file_path)
        user_input = user_interface.UserInterface()
        publication_text = user_input.ask_publication_text()
        publication_text = text_case_normalization.normalize_text_case(publication_text, '')
        expiration_date = user_input.ask_expiration_date()
        publications.Advertisement.write_advertisement(expiration_date, publication_text, file_path)
        print('The publication was published successfully.')
    except FileNotFoundError:
        print("Target file not found. Please check News_file.txt")


def publish_article(file_path):
    """
        Function for publishing of article scenario.
        Function creates objects of UserInterface, Article classes.
        Asks user to enter publication text, author.
        After writes entered data to file.
        Catches exception if target file not found.
    """
    try:
        publications_parser.PublicationsParser.check_file_path(file_path)
        user_input = user_interface.UserInterface()
        publication_text = user_input.ask_publication_text()
        publication_text = text_case_normalization.normalize_text_case(publication_text, '')
        author = user_input.ask_author()
        publications.Article.write_article(publication_text, author, file_path)
        print('The publication was published successfully.')
    except FileNotFoundError:
        print("Target file not found. Please check News_file.txt")


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
        if input_format == '1':
            publication_type = user_input.ask_publication_type()
            if publication_type == '1':
                publish_news(file_paths[1])
            elif publication_type == '2':
                publish_advertisement(file_paths[1])
            elif publication_type == '3':
                publish_article(file_paths[1])
            else:
                print('Please enter a number between 1 and 3. Try again please.')
                continue
            user_choice = input('Do you want to add more publications? Type "Yes" or "No":\n')
            if user_choice == 'Yes':
                continue
            elif user_choice == 'No':
                break
            else:
                print('Incorrect value entered.')
                break
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
                break
            else:
                print('Incorrect value entered.')
                break


# Application starting
if __name__ == '__main__':
    start()
