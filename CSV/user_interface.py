import datetime


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
