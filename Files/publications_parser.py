
import publications
import text_case_normalization
import datetime
import os
import argparse


class PublicationsParser:

    @staticmethod
    def parse_target_file(source_file_path, target_file_path):
        """
        Method takes file from source_file_path and takes all rows that start
        with "News" or "Advertisement" or "Article"
        then reformat them and writes to target_file_path.
        Method removes source file after processing.
        Method calculates count of published publication to file.
        @param source_file_path: path to file with publications
        @param target_file_path: path to target file for publishing
        """
        try:
            count_published = 0
            with open(f'{source_file_path}', 'r') as source_file:
                for _, line in enumerate(source_file):
                    if str(line).startswith('"News"') and str(line).endswith('.\n'):
                        publications_list = PublicationsParser.prepare_list(line)
                        publication_date = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
                        city = text_case_normalization.remove_prefixes(publications_list[2])
                        publication_text = PublicationsParser.prepare_text(publications_list)
                        publications.News.write_news(city, publication_date, publication_text, target_file_path)
                        count_published += 1
                    elif str(line).startswith('"Advertisement"') and str(line).endswith('.\n'):
                        publications_list = PublicationsParser.prepare_list(line)
                        expiration_date = text_case_normalization.remove_prefixes(publications_list[2])
                        publication_text = PublicationsParser.prepare_text(publications_list)
                        publications.Advertisement.write_advertisement(expiration_date, publication_text,
                                                                       target_file_path)
                        count_published += 1
                    elif str(line).startswith('"Article"') and str(line).endswith('.\n'):
                        publications_list = PublicationsParser.prepare_list(line)
                        publication_text = PublicationsParser.prepare_text(publications_list)
                        author = text_case_normalization.remove_prefixes(publications_list[2])
                        publications.Article.write_article(publication_text, author, target_file_path)
                        count_published += 1
                    else:
                        print('Unknown record type.')
            os.remove(source_file_path)
            print(f'{count_published} publications were published.')
        except FileNotFoundError:
            print('File not found. Please place file into target folder and try again.')

    @staticmethod
    def prepare_list(line):
        """
        Method creates a list from publication line. It deletes whitespaces and separate publications properties by ';'
        @param line: string with publication
        @return: list with publication properties
        """
        publications_list = str(line).strip().split('; ')
        return publications_list

    @staticmethod
    def prepare_text(publications_list):
        """
        Method takes list with publications removes prefixes and suffixes, normalize letter case
        and return formatted text.
        @param publications_list: publications list
        @return: normalized text
        """
        publication_text = text_case_normalization.remove_prefixes(publications_list[1])
        publication_text = text_case_normalization.normalize_text_case(publication_text, '')
        publication_text = f'{publication_text}' + '.'
        return publication_text

    @staticmethod
    def check_file_path(file_path):
        """
        Method validates file path provided by user. Only *.txt files allowed parsing.
        @param file_path: path to file with publications
        @return: return only valid path
        """
        try:
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
        except TypeError:
            print('Path to target publications file or default file not set in application parameters. '
                  'Please check --target_file_path and --default_path parameters and try again.')
            exit(1)

    @staticmethod
    def parse_files_paths():
        """
        Method reads --default_path and --target_file_path parameters and extract paths for further using.
        @return: default path, target file path
        """
        try:
            parser = argparse.ArgumentParser()
            parser.add_argument("--default_path", help='set the default path to file with publications for loading.')
            parser.add_argument("--target_file_path", help='set the target file path to file for publications writing.')
            arg = parser.parse_args()
            return arg.default_path, arg.target_file_path
        except Exception:
            print("Required parameters are missing!")
