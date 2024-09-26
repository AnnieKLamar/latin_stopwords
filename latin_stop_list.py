import sys
import pandas as pd
import csv


def get_latin_stop_list(lemmatized=True, returned_object='dataframe'):
    if lemmatized:
        with open('classical_latin_poetry_stop_words_lemmatized.txt') as f:
            if returned_object == 'list':
                return f.read().split(", ")
            elif returned_object == 'dataframe':
                return pd.DataFrame(list(csv.reader(f)))
    else:
        with open('classical_latin_poetry_stop_words_unlemmatized.txt') as f:
            if returned_object == 'list':
                return f.read().split(", ")
            elif returned_object == 'dataframe':
                return pd.DataFrame(list(csv.reader(f)))


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Get stop list for Classical Latin poetry.")
    parser.add_argument("lemmatized", help="True for lemmatized stop list, False for unlemmatized", type=bool,
                        default=True)
    parser.add_argument("returned_object", help="Type of object to return; options are dataframe or list",
                        default='dataframe')
    args = parser.parse_args()
    return get_latin_stop_list(args.lemmatized, args.returned_object)


if __name__ == '__main__':
    main()
