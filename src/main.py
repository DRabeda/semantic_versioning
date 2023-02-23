#Semantic versioning (np. 1.2.3, - MAJOR.MINOR.PATCH)
#Przechowując wersję w pliku napisz ponizszą logike.
#- napisz obsługę semantycznego wersjonowania:
    #- jezeli podasz do skryptu argument "major" - zwieksza wersje MAJOR
    #- MINOR i PATCH jak wyzej
    #- dodaj obsluge rollback - 'MAJOR rollback' - 2.2.2 -> 1.2.2
    #- jezeli wersji nie da sie zmniejszyc - zakoncz egzekucje bez robienia tego. (MAJOR rollback - 0.1.1 -> 0.1.1)
#
#Poczytaj o bibliotece 'argparse'.
#--version: print current version.
#--major --rollback: 2.2.2 -> 1.2.2
#--major: 1.2.2 -> 2.2.2
#--patch: 0.0.1 -> 0.0.2
#--minor: 0.1.1 -> 0.2.1
#
#python3 versioning.py --major --rollback

import argparse

major = argparse.ArgumentParser()
major.add_argument("--major", help="show more stats", action="store_true")
args = major.parse_args()

minor = argparse.ArgumentParser()
minor.add_argument("-a","--patch", help="show more stats", action="store_true")
args = minor.parse_args()


patch = argparse.ArgumentParser()
patch.add_argument("-a","--minor", help="show more stats", action="store_true")
args = patch.parse_args()

text_path = "version.txt"

def load_text(text_path: str):
        with open(text_path, "r") as stream:
            return stream.read()
        
load_text(text_path)