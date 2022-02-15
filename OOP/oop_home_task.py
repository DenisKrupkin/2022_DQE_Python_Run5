"""
Home task for Module 5 - Classes. OOP.

Create a tool, which will do user generated news feed:

1.User select what data type he wants to add

2.Provide record type required data

3.Record is published on text file in special format



You need to implement:

1.News – text and city as input. Date is calculated during publishing.

2.Private ad – text and expiration date as input. Day left is calculated during publishing.

3.Your unique one with unique publish rules.



Each new record should be added to the end of file. Commit file in git for review.
"""

import datetime

SEPARATOR = '------------------------------\n\n'


class Publication:
    """
    Class represents publication entity.
    """
    def __init__(self, publication_date, publication_type, city, publication_text):
        """
        Function is constructor for Publication.
        @param publication_date: date of publication
        @param publication_type: type of publication
        @param city: city where something happened
        @param publication_text: text of publication
        """
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
        """
        Method for entering of city for publication.
        @return: city entered by user
        """
        city = input("Where are you from? (City):\n")
        return city

    @staticmethod
    def ask_publication_type():
        """
        Method for entering the type of publication.
        @return: type of publication selected by user
        """
        publication_type = input("Please choose publication type (1-3): 1. News 2. Advertisement 3. Article\n")
        return publication_type

    @staticmethod
    def ask_publication_text():
        """
        Method for entering the publication text.
        @return: text of publication entered by user
        """
        publication_text = input("Please write text of publication: \n")
        return publication_text

    @staticmethod
    def ask_expiration_date():
        """
        Method for entering expiration date of publication.
        It validates format of entered dates. Correct format is only yyyy-mm-dd.
        If date is of incorrect format - catch exception and exit from application.
        @return: entered validated date
        """
        expiration_date = input("Please enter expiration date (yyyy-mm-dd): \n")
        try:
            datetime.datetime.strptime(expiration_date, '%Y-%m-%d')
            return expiration_date
        except ValueError:
            print('Incorrect date. Please use this format only: yyyy-mm-dd.')
            exit(-1)

    @staticmethod
    def ask_author():
        """
        Method for entering text author.
        @return: author of publication entered by user
        """
        author = input("Please enter your name: \n")
        return author


class News(Publication):
    """
    Class that represents the news publication type. Inherits Publication class.
    """
    def __init__(self, publication_date, city, publication_text, publication_type=1):
        """
        Method is constructor for news class
        @param publication_date: date of publication
        @param publication_type: type of publication
        @param city: city where something happened
        @param publication_text: text of publication
        """
        self.news_splitter = 'News -------------------------'
        super().__init__(city, publication_type, publication_date, publication_text)

    def publish_news(self):
        """
        Blank method for publishing of news that will be overwritten
        @return: nothing
        """
        pass


class Advertisement(Publication):
    """
    Class that represents the Advertisement publication type. Inherits Publication class.
    """
    def __init__(self, publication_date, expiration_date, publication_text, publication_type=2, city=''):
        """
        Method is constructor for Advertisement class
        @param publication_date: date of publication
        @param expiration_date: date of Advertisement expiration
        @param publication_text: text of publication
        @param publication_type: type of publication
        @param city: city where something happened
        """
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
            expiration_days = (datetime.date.today() - datetime.date.fromisoformat(expiration_date))*-1
            return expiration_days.days
        except TypeError:
            print('Expiration days calculation error.')

    def publish_advertisement(self):
        """
        Blank method for publishing of Advertisement that will be overwritten
        @return: nothing
        """
        pass


class Article(Publication):
    """
    Class that represents the Article publication type. Inherits Publication class.
    """
    def __init__(self, publication_text, author, publication_date=None, publication_type=3, city=None):
        """
        Method is constructor for Advertisement class
        @param publication_text: text of publication
        @param author: author of publication
        @param publication_date: date of publication
        @param publication_type: type of publication
        @param city: city where something happened
        """
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

    def publish_article(self):
        """
        Blank method for publishing of Article that will be overwritten
        @return: nothing
        """
        pass


class ObjectsCreator:
    """
    Class for objects creation
    """
    @staticmethod
    def create_news(city, publication_date, publication_text):
        """
        Creates a new news object with specified set of parameters
        @param city: city where something happened
        @param publication_date: date of publication
        @param publication_text: text of publication
        @return: created news object
        """
        news = News(city, publication_date, publication_text)
        return news

    @staticmethod
    def create_advertisement(publication_date, expiration_date, publication_text):
        """
        Creates a new advertisement object with specified set of parameters
        @param publication_date: date of publication
        @param expiration_date: date when adv will expire
        @param publication_text: text of publication
        @return: created advertisement object
        """
        advertisement = Advertisement(publication_date, expiration_date, publication_text)
        return advertisement

    @staticmethod
    def create_article(publication_text, author):
        """
        Creates a new article object with specified set of parameters
        @param publication_text: text of publication
        @param author: author of article
        @return: created article object
        """
        article = Article(publication_text, author)
        return article


class FileWriter:
    """
    Class for writing to text file
    """
    @staticmethod
    def open_file(file_name):
        """
        Open file for writing
        @param file_name: file name
        @return: opened file object
        """
        publications_file = open(f'{file_name}', 'a')
        return publications_file

    @staticmethod
    def write_heading(publications_file, heading):
        """
        Writes heading of publication to file
        @param publications_file: opened file object
        @param heading: heading of publication
        """
        publications_file.write(f'{heading}\n')

    @staticmethod
    def write_publication_text(publications_file, text):
        """
        Writes text of publication to file
        @param publications_file: opened file object
        @param text: text of publication
        """
        publications_file.write(f'{text}\n')

    @staticmethod
    def write_publication_date(publications_file, publication_date):
        """
        Writes date of publication to file
        @param publications_file: opened file object
        @param publication_date: date of publication
        """
        publications_file.write(f'{publication_date}\n')

    @staticmethod
    def write_city(publications_file, city):
        """
        Writes city of publication to file
        @param publications_file: opened file object
        @param city: city of publication
        """
        publications_file.write(f'{city}, ')

    @staticmethod
    def write_expiration_date(publications_file, expiration_date):
        """
        Writes expiration date of publication to file
        @param publications_file: opened file object
        @param expiration_date: date of publication
        """
        publications_file.write(f'Actual until: {expiration_date}, ')

    @staticmethod
    def write_expiration_days(publications_file, expiration_days):
        """
        Writes expiration days of publication to file
        @param publications_file: opened file object
        @param expiration_days: date of publication
        """
        publications_file.write(f'{expiration_days} days left\n')

    @staticmethod
    def write_author(publications_file, author):
        """
        Writes author of publication to file
        @param publications_file: opened file object
        @param author: author of publication
        """
        publications_file.write(f'Text author: {author}. ')

    @staticmethod
    def write_text_total_symbols(publications_file, symbols_count):
        """
        Writes count of symbols in publication text to file
        @param publications_file: opened file object
        @param symbols_count: count of symbols
        """
        publications_file.write(f'Symbols count: {symbols_count}.\n')

    @staticmethod
    def write_ending(publications_file, separator):
        """
        Writes publications separator to file
        @param publications_file: opened file object
        @param separator: publications SEPARATOR
        """
        publications_file.write(f'{separator}')
        pass

    @staticmethod
    def close_file(publications_file):
        """
        Closes publications file
        @param publications_file: opened file object
        """
        publications_file.close()


class Application(News, Advertisement, Article):
    """
    Class Application that inherits News, Advertisement, Article classes.
    Used for creation of final publication scenarios and running of application.
    """
    def __init__(self, city='', publication_text='', publication_date=''):
        """
        Method is constructor for Application class
        @param publication_text: text of publication, empty by default
        @param publication_date: date of publication, empty by default
        @param city: city where something happened, empty by default
        """
        super().__init__(publication_date, city, publication_text)

    def publish_news(self):
        """
        Method for publishing of news scenario.
        Method creates objects of UserInterface, FileWriter, ObjectCreator classes.
        Asks user to enter publication text, city.
        After writes entered data to file in turn using FileWriter methods.
        Catches exception if target file not found.
        """
        try:
            user_interface = UserInterface()
            file_writer = FileWriter()
            file = file_writer.open_file('News_file.txt')
            publication_text = user_interface.ask_publication_text()
            city = user_interface.ask_city()
            publication_date = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
            creator = ObjectsCreator()
            news = creator.create_news(city, publication_date, publication_text)
            file_writer.write_heading(file, news.news_splitter)
            file_writer.write_publication_text(file, news.publication_text)
            file_writer.write_city(file, news.city)
            file_writer.write_publication_date(file, news.publication_date)
            file_writer.write_ending(file, SEPARATOR)
            file_writer.close_file(file)
        except FileNotFoundError:
            print("Target file not found. Please check News_file.txt")

    def publish_advertisement(self):
        """
        Method for publishing of advertisement scenario.
        Method creates objects of UserInterface, FileWriter, ObjectCreator classes.
        Asks user to enter publication text, expiration date.
        After writes entered data to file in turn using FileWriter methods.
        Catches exception if target file not found.
        """
        try:
            user_interface = UserInterface()
            file_writer = FileWriter()
            file = file_writer.open_file('News_file.txt')
            publication_text = user_interface.ask_publication_text()
            expiration_date = user_interface.ask_expiration_date()
            publication_date = datetime.datetime.today()
            creator = ObjectsCreator()
            advertisement = creator.create_advertisement(publication_date, expiration_date, publication_text)
            file_writer.write_heading(file, advertisement.advertisement_splitter)
            file_writer.write_publication_text(file, advertisement.publication_text)
            file_writer.write_expiration_date(file, expiration_date)
            file_writer.write_expiration_days(file, advertisement.calculate_expiration_days(expiration_date))
            file_writer.write_ending(file, SEPARATOR)
            file_writer.close_file(file)
        except FileNotFoundError:
            print("Target file not found. Please check News_file.txt")

    def publish_article(self):
        """
        Method for publishing of article scenario.
        Method creates objects of UserInterface, FileWriter, ObjectCreator classes.
        Asks user to enter publication text, author.
        After writes entered data to file in turn using FileWriter methods.
        Catches exception if target file not found.
        """
        try:
            user_interface = UserInterface()
            file_writer = FileWriter()
            file = file_writer.open_file('News_file.txt')
            publication_text = user_interface.ask_publication_text()
            author = user_interface.ask_author()
            creator = ObjectsCreator()
            article = creator.create_article(publication_text, author)
            file_writer.write_heading(file, article.article_splitter)
            file_writer.write_publication_text(file, article.publication_text)
            file_writer.write_author(file, article.author)
            file_writer.write_text_total_symbols(file, article.calculate_symbols_count(publication_text))
            file_writer.write_ending(file, SEPARATOR)
            file_writer.close_file(file)
        except FileNotFoundError:
            print("Target file not found. Please check News_file.txt")

    @staticmethod
    def start():
        """
        Method for application starting.
        Method asks user to select publication type.
        After publication finished asks user to choose "Yes" for continue or stop publishing answering "No".
        Catches exception if user answered something else except "Yes" or "No".
        """
        while True:
            user_interface = UserInterface()
            publication_type = user_interface.ask_publication_type()
            if publication_type == '1':
                application.publish_news()
            elif publication_type == '2':
                application.publish_advertisement()
            elif publication_type == '3':
                application.publish_article()
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


# Application starting
if __name__ == '__main__':
    application = Application()
    application.start()
