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
            expiration_days = (datetime.date.today() - datetime.date.fromisoformat(expiration_date))*-1
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


class Application(News, Advertisement, Article):
    """
    Class Application that inherits News, Advertisement, Article classes.
    Used for creation of final publication scenarios and running of application.
    """
    def __init__(self, city='', publication_text='', publication_date=''):
        super().__init__(publication_date, city, publication_text)

    @staticmethod
    def publish_news():
        """
        Method for publishing of news scenario.
        Method creates objects of UserInterface, News classes.
        Asks user to enter publication text, city.
        After writes entered data to file.
        Catches exception if target file not found.
        """
        try:
            user_interface = UserInterface()
            with open('News_file.txt', 'a') as publications_file:
                publication_text = user_interface.ask_publication_text()
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

    @staticmethod
    def publish_advertisement():
        """
        Method for publishing of advertisement scenario.
        Method creates objects of UserInterface, Advertisement classes.
        Asks user to enter publication text, expiration date.
        After writes entered data to file.
        Catches exception if target file not found.
        """
        try:
            user_interface = UserInterface()
            with open('News_file.txt', 'a') as publications_file:
                publication_text = user_interface.ask_publication_text()
                expiration_date = user_interface.ask_expiration_date()
                advertisement = Advertisement(expiration_date, publication_text)
                publications_file.write(f'{advertisement.advertisement_splitter}\n')
                publications_file.write(f'{advertisement.publication_text}\n')
                publications_file.write(f'Actual until: {expiration_date}, ')
                publications_file.write(f'{advertisement.calculate_expiration_days(expiration_date)} days left\n')
                publications_file.write(f'{SEPARATOR}')
        except FileNotFoundError:
            print("Target file not found. Please check News_file.txt")

    @staticmethod
    def publish_article():
        """
        Method for publishing of article scenario.
        Method creates objects of UserInterface, Article classes.
        Asks user to enter publication text, author.
        After writes entered data to file.
        Catches exception if target file not found.
        """
        try:
            user_interface = UserInterface()
            with open('News_file.txt', 'a') as publications_file:
                publication_text = user_interface.ask_publication_text()
                author = user_interface.ask_author()
                article = Article(publication_text, author)
                publications_file.write(f'{article.article_splitter}\n')
                publications_file.write(f'{article.publication_text}\n')
                publications_file.write(f'Text author: {article.author}. ')
                publications_file.write(f'Symbols count: {article.calculate_symbols_count(publication_text)}.\n')
                publications_file.write(f'{SEPARATOR}')
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
