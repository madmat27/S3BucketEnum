#! /usr/bin/env python3

# Imports που χρειάζεται το πρόγραμμα για να δουλέψει
import argparse
import requests
import sys
import time
from prettytable import PrettyTable
from termcolor import colored
from tqdm import tqdm


# Μηνύματα σφάλματος που εμφανίζονται στο πρόγραμμα
file_type_error = 'Invalid file type. Please use a .txt file only'
file_not_found_error = 'There is no such file. Please check path and/or filename'


def show_header():
    """
    Εμφανίζει το logo του προγράμματος
    :argument: κανένα
    :return: τίποτα
    """
    print(colored(' ', 'blue').ljust(80))
    print(colored('   __________ ____             __        __  ______                     ', 'blue').ljust(80))
    print(colored('  / ___/__  // __ )__  _______/ /_____  / /_/ ____/___  __  ______ ___  ', 'blue').ljust(80))
    print(colored('  \__ \ /_ </ __  / / / / ___/ //_/ _ \/ __/ __/ / __ \/ / / / __ `__ \ ', 'blue').ljust(80))
    print(colored(' ___/ /__/ / /_/ / /_/ / /__/ ,< /  __/ /_/ /___/ / / / /_/ / / / / / / ', 'blue').ljust(80))
    print(colored('/____/____/_____/\__,_/\___/_/|_|\___/\__/_____/_/ /_/\__,_/_/ /_/ /_/  ', 'blue').ljust(80))
    print(colored(' ', 'blue').ljust(80))
    print(colored('  AWS S3 Bucket Enumerator                        ', 'cyan').ljust(80))
    print(colored('  Mariana S. Mazi @madmat27', 'cyan').ljust(80))
    print(colored(' ', 'blue').ljust(80))


def additional_help_message():
    """
    Εμφάνιση επιπλέον οδηγιών για τη μορφή του text αρχείου που δέχεται ως είσοδο το πρόγραμμα
    :argument: κανένα
    :return: τίποτα
    """

    # Εμφανίζει το μήνυμα βοήθειας, για τη σωστή δομή του αρχείου .txt
    print(colored('Structure of file is not correct. Please check the following:', 'red'))
    print(colored('1. Parameter is an actual text (.txt) file - not just the extension', 'yellow'))
    print(colored('2. Each line has only one word/name. Words/names separated with commas, '
                  'colons or periods are not valid', 'yellow'))
    print(colored('3. Only text files are allowed; no .json or .csv files', 'yellow'))


def open_format_wlist(wordlist):
    """
    Ανοίγει το text αρχείο που δόθηκε ως λίστα και το μορφοποιεί
    :param wordlist: Το αρχείο .txt που χρειάζεται η συνάρτηση για να δημιουργήσει τη λίστα
    :return: s_wlst: Η μορφοποιημένη λίστα με τα ονόματα του .txt αρχείου
    """

    wordlist_file = wordlist

    # Διαχείριση σφαλμάτων
    try:
        # Ανοίγει το αρχείο txt
        fd = open(wordlist_file, 'r')
        wlist = fd.readlines()
        new_wlst = [x[:-1] for x in wlist]
        # Μετατρέπει όλη τη λίστα σε πεζούς χαρακτήρες
        s_wlst = []
        for w in new_wlst:
            s_wlst.append(w.lower())
        # Ταξινομεί τη λίστα κατά αύξουσα σειρά
        s_wlst = sorted(s_wlst)
        return s_wlst
    # Σε περίπτωση των παρακάτω σφαλμάτων, εκτυπώνονται τα αντίστοιχα μηνύματα
    except UnicodeDecodeError:
        print(colored(file_type_error, 'red'))
        sys.exit(1)
    except FileNotFoundError:
        print(colored(file_not_found_error, 'red'))
        sys.exit(1)


def bucket_enum(wordlist):
    """
    Για κάθε στοιχείο της λίστας, δοκιμάζει το όνομα στο URL "s3.amazonaws.com", για να δούμε αν υπάρχει το bucket
    και τι δικαιώματα έχει
    :param wordlist: Η μορφοποιημένη λίστα με τα ονόματα
    :return: Τίποτα - εκτυπώνει τα αποτελέσματα στην οθόνη
    """

    # Δημιουργία πίνακα αποτελεσμάτων
    result_table = PrettyTable(["URL", "STATUS"])

    # Διαχείριση σφαλμάτων
    try:
        # Για κάθε στοιχείο της λίστας:
        # α. Δημιουργία μπάρας προόδου (tqdm)
        # β. Αποστολή αιτήματος στο URL και εγγραφή στον πίνακα αποτελεσμάτων του URL και της κατάστασης
        for i, w in zip(tqdm(range(len(wordlist)),
                             desc="Loading…",
                             ascii=False, ncols=75), wordlist):
            time.sleep(0.01)
            response = requests.get('https://' + w + '.s3.amazonaws.com')
            if "AccessDenied" in str(response.content):
                status = "Bucket exists and is private"
                result_table.add_row([response.url, status])
            elif "AllAccessDisabled" in str(response.content):
                status = "Bucket exist and all access is disabled."
                result_table.add_row([response.url, status])
            elif "NoSuchBucket" in str(response.content):
                status = "Bucket doesn't exist."
                result_table.add_row([response.url, status])
            else:
                status = "Bucket is public and listable!"
                result_table.add_row([response.url, status])

        # Εκτύπωση πίνακα με τα αποτελέσματα
        print(result_table)
    # Σε περίπτωση των παρακάτω σφαλμάτων, εκτυπώνονται τα αντίστοιχα μηνύματα
    except UnicodeError:
        print(colored(file_type_error, 'red'))
        additional_help_message()
        sys.exit(1)
    except requests.exceptions.InvalidURL:
        additional_help_message()
        sys.exit(1)


if __name__ == '__main__':

    # Εμφάνιση αρχικής κεφαλίδας
    show_header()

    # Ορισμός υποχρεωτικής παραμέτρου του προγράμματος
    parser = argparse.ArgumentParser(prog="S3BucketEnum",
                                     description="AWS S3 Bucket Enumerator",
                                     epilog="Feel free to pass the code!",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("wlist", help="Specify a .txt wordlist file to be used to enumerate S3 buckets")
    args = parser.parse_args()
    config = vars(args)
    print(config)

    # Εκτέλεση προγράμματος
    bucket_enum(open_format_wlist(config.get('wlist')))
