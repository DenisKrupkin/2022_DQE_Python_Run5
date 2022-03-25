"""
Home task for Module 6 - Module. Files.

Expand previous Homework 5 with additional class, which allow providing records by text file:

1.Define your input format (one or many records)

2.Default folder or user provided file path

3.Remove file if it was successfully processed

4.Apply case normalization functionality form Homework 3/4
"""

import datetime
import os
import text_case_normalization

SEPARATOR = '------------------------------\n\n'


# Main classes:


class Publication:
    """
    Class represents publication entity.
    """

    def __init__(self, publication_date, publication_type, city, publication_text):
        self.publication_date = publication_date
        self.publication_type = publication_type
        self.city = city
        self.publication_text = publication_text


class UserInterface:
    """
    Class for interaction with user inputs.
    """

    @staticmethod
    def ask_city():
        city = input("Where are you from? (City):\n")
        return city

    @staticmethod
    def ask_publication_type():
        publication_type = input("Please choose publication type (1-3): 1. News 2. Advertisement 3. Article\n")
        return publication_type

    @staticmethod
    def ask_publication_text():
        publication_text = input("Please write text of publication: \n")
        return publication_text

    @staticmethod
    def ask_expiration_date():
        expiration_date = input("Please enter expiration date (yyyy-mm-dd): \n")
        try:
            datetime.datetime.strptime(expiration_date, '%Y-%m-%d')
            return expiration_date
        except ValueError:
            print('Incorrect date. Please use this format only: yyyy-mm-dd.')
            exit(-1)

    @staticmethod
    def ask_author():
        author = input("Please enter your name: \n")
        return author

    @staticmethod
    def ask_input_format():
        input_format = input("Please choose input format (1-2): 1. One record 2. Many records (load from file)\n")
        return input_format

    @staticmethod
    def ask_file_path_mode():
        file_path_mode = input("Please choose using default file path or custom one (1-2): 1. Default 2. Custom\n")
        return file_path_mode

    @staticmethod
    def ask_file_path():
        file_path = input("Please enter path to file with publications: \n")
        return file_path


class News(Publication):
    """
    Class that represents the news publication type. Inherits Publication class.
    """

    def __init__(self, publication_date, city, publication_text, publication_type=1):
        self.news_splitter = 'News -------------------------'
        super().__init__(city, publication_type, publication_date, publication_text)


class Advertisement(Publication):
    """
    Class that represents the Advertisement publication type. Inherits Publication class.
    """

    def __init__(self, expiration_date, publication_text, publication_date=None, publication_type=2, city=None):
        self.advertisement_splitter = 'Private Ad -------------------'
        self.expiration_date = expiration_date
        super().__init__(publication_date, publication_type, city, publication_text)

    @staticmethod
    def calculate_expiration_days(expiration_date):
        """
        Method for expiration days calculation. Catches TypeError exception.
        @param expiration_date: date of Advertisement expiration
        @return: count of days from today to expiration date
        """
        try:
            expiration_days = (datetime.date.today() - datetime.date.fromisoformat(expiration_date)) * -1
            return expiration_days.days
        except TypeError:
            print('Expiration days calculation error.')


class Article(Publication):
    """
    Class that represents the Article publication type. Inherits Publication class.
    """

    def __init__(self, publication_text, author, publication_date=None, publication_type=3, city=None):
        self.author = author
        self.article_splitter = 'Article ----------------------'
        super().__init__(publication_date, publication_type, city, publication_text)

    @staticmethod
    def calculate_symbols_count(publication_text):
        """
        Method that calculated total of alphanumeric symbols in text entered as Article.
        @param publication_text: text of publication
        @return: total symbols count
        """
        symbols_count = 0
        for symbol in publication_text:
            if symbol.isalnum():
                symbols_count += 1
        return symbols_count


class PublicationsParser:

    @staticmethod
    def parse_target_file(file_path):
        """
        Method takes file from file_path and takes all rows that start with "News" or "Advertisement" or "Article"
        then reformat them and writes to target News_file.txt file.
        @param file_path: path to file with publications
        """
        try:
            text_case_normalizer = text_case_normalization.TextCaseNormalizer()
            with open(f'{file_path}', 'r') as source_file:
                for line_number, line in enumerate(source_file):
                    if str(line).startswith('"News"') and str(line).endswith('.\n'):
                        publications_list = str(line).strip().split('; ')
                        publication_date = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
                        city = publications_list[2].removeprefix('"').removesuffix('".')
                        publication_text = publications_list[1].removeprefix('"').removesuffix('"')
                        publication_text = text_case_normalizer.normalize_text_case(publication_text, '')
                        news = News(city, publication_date, publication_text)
                        with open('News_file.txt', 'a') as publications_file:
                            publications_file.write(f'{news.news_splitter}\n')
                            publications_file.write(f'{news.publication_text}\n')
                            publications_file.write(f'{news.city}, ')
                            publications_file.write(f'{news.publication_date}\n')
                            publications_file.write(f'{SEPARATOR}')
                    elif str(line).startswith('"Advertisement"') and str(line).endswith('.\n'):
                        publications_list = str(line).strip().split('; ')
                        expiration_date = publications_list[2].removeprefix('"').removesuffix('".')
                        publication_text = publications_list[1].removeprefix('"').removesuffix('"')
                        publication_text = text_case_normalizer.normalize_text_case(publication_text, '')
                        advertisement = Advertisement(expiration_date, publication_text)
                        with open('News_file.txt', 'a') as publications_file:
                            publications_file.write(f'{advertisement.advertisement_splitter}\n')
                            publications_file.write(f'{advertisement.publication_text}\n')
                            publications_file.write(f'Actual until: {expiration_date}, ')
                            publications_file.write(
                                f'{advertisement.calculate_expiration_days(expiration_date)} days left\n')
                            publications_file.write(f'{SEPARATOR}')
                    elif str(line).startswith('"Article"') and str(line).endswith('.\n'):
                        publications_list = str(line).strip().split('; ')
                        publication_text = publications_list[1].removeprefix('"').removesuffix('"')
                        publication_text = text_case_normalizer.normalize_text_case(publication_text, '')
                        author = publications_list[2].removeprefix('"').removesuffix('".')
                        article = Article(publication_text, author)
                        with open('News_file.txt', 'a') as publications_file:
                            publications_file.write(f'{article.article_splitter}\n')
                            publications_file.write(f'{article.publication_text}\n')
                            publications_file.write(f'Text author: {article.author}. ')
                            publications_file.write(
                                f'Symbols count: {article.calculate_symbols_count(publication_text)}.\n')
                            publications_file.write(f'{SEPARATOR}')
                    else:
                        print('Unknown record type.')
            os.remove(file_path)
        except FileNotFoundError:
            print('File not found. Please place file into target folder and try again.')

    @staticmethod
    def check_file_path(file_path):
        """
        Method validates file path provided by user. Only *.txt files allowed parsing.
        @param file_path: path to file with publications
        @return: return only valid path
        """
        if os.path.exists(file_path):
            if os.path.isfile(file_path):
                if str(file_path).lower().endswith('.txt'):
                    return file_path
                else:
                    print(f'Provided path:\n"{file_path}"\nFile should be in *.txt format.')
                    exit(1)
            elif os.path.isdir(file_path):
                print(f'This path:\n"{file_path}"\nto catalog only. Please enter full path to file.')
                exit(1)
        else:
            print(f'Incorrect or empty file path:\n"{file_path}"')
            exit(1)

    @staticmethod
    def parse_default_path():
        """
        Method reads --default_path parameter and store the path for further using.
        @return: default path
        """
        import argparse
        parser = argparse.ArgumentParser()
        parser.add_argument("--default_path", help='set the default path to file with publications.')
        arg = parser.parse_args()
        return arg.default_path


# Publishing functions:


def publish_news():
    """
        Function for publishing of news scenario.
        Function creates objects of UserInterface, News classes.
        Asks user to enter publication text, city.
        After writes entered data to file.
        Catches exception if target file not found.
    """
    try:
        user_interface = UserInterface()
        text_case_normalizer = text_case_normalization.TextCaseNormalizer()
        with open('News_file.txt', 'a') as publications_file:
            publication_text = user_interface.ask_publication_text()
            publication_text = text_case_normalizer.normalize_text_case(publication_text, '')
            city = user_interface.ask_city()
            publication_date = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
            news = News(city, publication_date, publication_text)
            publications_file.write(f'{news.news_splitter}\n')
            publications_file.write(f'{news.publication_text}\n')
            publications_file.write(f'{news.city}, ')
            publications_file.write(f'{news.publication_date}\n')
            publications_file.write(f'{SEPARATOR}')
    except FileNotFoundError:
        print("Target file not found. Please check News_file.txt")


def publish_advertisement():
    """
        Function for publishing of advertisement scenario.
        Function creates objects of UserInterface, Advertisement classes.
        Asks user to enter publication text, expiration date.
        After writes entered data to file.
        Catches exception if target file not found.
    """
    try:
        user_interface = UserInterface()
        text_case_normalizer = text_case_normalization.TextCaseNormalizer()
        with open('News_file.txt', 'a') as publications_file:
            publication_text = user_interface.ask_publication_text()
            publication_text = text_case_normalizer.normalize_text_case(publication_text, '')
            expiration_date = user_interface.ask_expiration_date()
            advertisement = Advertisement(expiration_date, publication_text)
            publications_file.write(f'{advertisement.advertisement_splitter}\n')
            publications_file.write(f'{advertisement.publication_text}\n')
            publications_file.write(f'Actual until: {expiration_date}, ')
            publications_file.write(f'{advertisement.calculate_expiration_days(expiration_date)} days left\n')
            publications_file.write(f'{SEPARATOR}')
    except FileNotFoundError:
        print("Target file not found. Please check News_file.txt")


def publish_article():
    """
        Function for publishing of article scenario.
        Function creates objects of UserInterface, Article classes.
        Asks user to enter publication text, author.
        After writes entered data to file.
        Catches exception if target file not found.
    """
    try:
        user_interface = UserInterface()
        text_case_normalizer = text_case_normalization.TextCaseNormalizer()
        with open('News_file.txt', 'a') as publications_file:
            publication_text = user_interface.ask_publication_text()
            publication_text = text_case_normalizer.normalize_text_case(publication_text, '')
            author = user_interface.ask_author()
            article = Article(publication_text, author)
            publications_file.write(f'{article.article_splitter}\n')
            publications_file.write(f'{article.publication_text}\n')
            publications_file.write(f'Text author: {article.author}. ')
            publications_file.write(f'Symbols count: {article.calculate_symbols_count(publication_text)}.\n')
            publications_file.write(f'{SEPARATOR}')
    except FileNotFoundError:
        print("Target file not found. Please check News_file.txt")


def start():
    """
        Function for application starting.
        Function asks user to select publications input format and after according to choice loads or writes
        publications to target file.
        After publication finished asks user to choose "Yes" for continue or stop publishing answering "No".
        Catches exception if user answered something else except "Yes" or "No".
        Takes --default_path parameter on starting to parse file with publications if user selected such input format.
        """
    while True:
        user_interface = UserInterface()
        input_format = user_interface.ask_input_format()
        if input_format == '1':
            publication_type = user_interface.ask_publication_type()
            if publication_type == '1':
                publish_news()
            elif publication_type == '2':
                publish_advertisement()
            elif publication_type == '3':
                publish_article()
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
            file_path_mode = user_interface.ask_file_path_mode()
            if file_path_mode == '1':
                publications_parser = PublicationsParser()
                try:
                    publications_parser.check_file_path(publications_parser.parse_default_path())
                    publications_parser.parse_target_file(publications_parser.parse_default_path())
                except TypeError:
                    print('Default path is not set as parameter. '
                          'Set "--default_path <path to file>" parameter and try again.')
                except Exception:
                    print('Unknown error occurred. Check the --default_path parameter.')
            elif file_path_mode == '2':
                file_path = user_interface.ask_file_path()
                publications_parser = PublicationsParser()
                publications_parser.check_file_path(file_path)
                publications_parser.parse_target_file(file_path)
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
