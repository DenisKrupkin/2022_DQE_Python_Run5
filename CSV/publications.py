import datetime
import user_interface
import text_case_normalization
import publications_parser


class Publication:
    """
    Class represents publication entity.
    """

    separator = '------------------------------\n\n'

    def __init__(self, publication_date, publication_type, city, publication_text):
        self.publication_date = publication_date
        self.publication_type = publication_type
        self.city = city
        self.publication_text = publication_text


class News(Publication):
    """
    Class that represents the news publication type. Inherits Publication class.
    """

    def __init__(self, publication_date, city, publication_text, publication_type=1):
        self.news_splitter = 'News -------------------------'
        super().__init__(city, publication_type, publication_date, publication_text)

    @staticmethod
    def write_news(city, publication_date, publication_text, target_file):
        """
        Method writes News to target file.
        @param city: city of publication
        @param publication_date: date of publication
        @param publication_text: text of publication
        @param target_file: file for publishing
        """
        publication = Publication
        news = News(city, publication_date, publication_text)
        with open(f'{target_file}', 'a') as publications_file:
            publications_file.write(f'{news.news_splitter}\n')
            publications_file.write(f'{news.publication_text}\n')
            publications_file.write(f'{news.city}, ')
            publications_file.write(f'{news.publication_date}\n')
            publications_file.write(f'{publication.separator}')

    @staticmethod
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
            News.write_news(city, publication_date, publication_text, file_path)
            print('The publication was published successfully.')
        except FileNotFoundError:
            print("Target file not found. Please check News_file.txt")


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

    @staticmethod
    def write_advertisement(expiration_date, publication_text, target_file):
        """
        Method writes Advertisement to target file.
        @param expiration_date: expiration date
        @param publication_text: publication text
        @param target_file: file for publishing
        """
        publication = Publication
        advertisement = Advertisement(expiration_date, publication_text)
        with open(f'{target_file}', 'a') as publications_file:
            publications_file.write(f'{advertisement.advertisement_splitter}\n')
            publications_file.write(f'{advertisement.publication_text}\n')
            publications_file.write(f'Actual until: {expiration_date}, ')
            publications_file.write(
                f'{advertisement.calculate_expiration_days(expiration_date)} days left\n')
            publications_file.write(f'{publication.separator}')

    @staticmethod
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
            Advertisement.write_advertisement(expiration_date, publication_text, file_path)
            print('The publication was published successfully.')
        except FileNotFoundError:
            print("Target file not found. Please check News_file.txt")


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

    @staticmethod
    def write_article(publication_text, author, target_file):
        """
        Method writes Article to target file.
        @param publication_text: text of publication
        @param author: article author
        @param target_file: file for publishing
        """
        publication = Publication
        article = Article(publication_text, author)
        with open(f'{target_file}', 'a') as publications_file:
            publications_file.write(f'{article.article_splitter}\n')
            publications_file.write(f'{article.publication_text}\n')
            publications_file.write(f'Text author: {article.author}. ')
            publications_file.write(
                f'Symbols count: {article.calculate_symbols_count(publication_text)}.\n')
            publications_file.write(f'{publication.separator}')

    @staticmethod
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
            Article.write_article(publication_text, author, file_path)
            print('The publication was published successfully.')
        except FileNotFoundError:
            print("Target file not found. Please check News_file.txt")
