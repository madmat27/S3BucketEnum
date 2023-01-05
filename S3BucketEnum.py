#! /usr/bin/env python3

# Imports που χρειάζεται το πρόγραμμα για να δουλέψει
import argparse
import requests
import time
from prettytable import PrettyTable
from tqdm import tqdm


def show_header():
    """
    Εμφανίζει το logo του προγράμματος
    :argument: κανένα
    :return: τίποτα
    """
    print(" ".ljust(80))
    print("   __________ ____             __        __  ______                     ".ljust(80))
    print("  / ___/__  // __ )__  _______/ /_____  / /_/ ____/___  __  ______ ___  ".ljust(80))
    print("  \__ \ /_ </ __  / / / / ___/ //_/ _ \/ __/ __/ / __ \/ / / / __ `__ \ ".ljust(80))
    print(" ___/ /__/ / /_/ / /_/ / /__/ ,< /  __/ /_/ /___/ / / / /_/ / / / / / / ".ljust(80))
    print("/____/____/_____/\__,_/\___/_/|_|\___/\__/_____/_/ /_/\__,_/_/ /_/ /_/  ".ljust(80))
    print(" ".ljust(80))
    print("  AWS S3 Bucket Enumerator                        ".ljust(80))
    print("  Mariana S. Mazi @madmat27".ljust(80))
    print(" ".ljust(80))


def open_format_wlist(wordlist):
    """
    Ανοίγει το text αρχείο που δόθηκε ως λίστα και το μορφοποιεί
    :param wordlist: Το αρχείο .txt που χρειάζεται η συνάρτηση για να δημιουργήσει τη λίστα
    :return: s_wlst: Η μορφοποιημένη λίστα με τα ονόματα του .txt αρχείου
    """

    wordlist_file = wordlist

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


def bucket_enum(wordlist):
    """
    Για κάθε στοιχείο της λίστας, δοκιμάζει το όνομα στο URL "s3.amazonaws.com", για να δούμε αν υπάρχει το bucket
    και τι δικαιώματα έχει
    :param wordlist: Η μορφοποιημένη λίστα με τα ονόματα
    :return: Τίποτα - εκτυπώνει τα αποτελέσματα στην οθόνη
    """

    # Δημιουργία πίνακα αποτελεσμάτων
    result_table = PrettyTable(["URL", "STATUS"])

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


if __name__ == '__main__':

    # Εμφάνιση αρχικής κεφαλίδας
    show_header()

    # Ορισμός υποχρεωτικών παραμέτρων προγράμματος
    parser = argparse.ArgumentParser(prog="S3BucketEnum",
                                     description="AWS S3 Bucket Enumerator",
                                     epilog="Feel free to pass the code!",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("wlist", help="Specify a wordlist to be used to enumerate S3 buckets")
    args = parser.parse_args()
    config = vars(args)
    print(config)

    # Εκτέλεση προγράμματος
    bucket_enum(open_format_wlist(config.get('wlist')))
