from re import match
from sys import exit
import csv


def dictionary():
    info()
    choosen_action = choosing_action()
    if choosen_action == "1":
        appellation = input("\nEnter appellation: ")
        search_by_appellation(appellation)
    elif choosen_action == "2":
        add_definition()
    elif choosen_action == "3":
        show_alphabetically()
    elif choosen_action == "4":
        letter = input("\nEnter first letter of appellation: ").lower()
        while not match("^[a-z]$", letter):
            letter = input("\nWrong input. Enter single letter: ").lower()
        show_by_letter(letter)
    else:
        exit()
    answer = continue_or_exit()
    if answer == "yes":
        dictionary()
    else:
        exit()


def info():
    print("\nDictionary for a little programmer:\n"
          "1) search explanation by appellation\n"
          "2) add new definition\n"
          "3) show all appellations alphabetically\n"
          "4) show available definitions by first letter of appellation\n"
          "0) exit\n")


def choosing_action():
    choosen_action = input("\nChoose action number: ")
    while not match("^[0-4]$|^exit$", choosen_action):
        print("\nWrong input. Choose number between 0 and 4")
        choosen_action = input("\nChoose action number: ")
    return choosen_action


def search_by_appellation(appellation):
    dictionary = open("dictionary.csv", "r")
    dictionary_reader = csv.reader(dictionary, delimiter=";")
    dictionary_data = list(dictionary_reader)
    definition_and_source = None
    for row in dictionary_data:
        if appellation == row[0]:
            definition_and_source = ("\n{}\n\n{}\n\nSource: {}\n".format(appellation.upper(), row[1], row[2]))
            break
    if definition_and_source is not None:
        print(definition_and_source)
    else:
        print("\nThere is no \"{}\" appellation in dictionary.\n".format(appellation))
    dictionary.close()


def add_definition():
    print("\nADDING DEFINITION TO DICTIONARY")
    appellation = input("\nEnter appellation: ").lower()
    definition = input("\nEnter definition: ")
    source = input("\nEnter source: ")

    dictionary = open("dictionary.csv", "a")
    dictionary_writer = csv.writer(dictionary, delimiter=";")
    dictionary_writer.writerow([appellation, definition, source])
    dictionary.close()

    print("\n\n{} added.\n".format(appellation.upper()))


def show_alphabetically():
    dictionary = open("dictionary.csv", "r")
    dictionary_reader = dictionary_reader = csv.reader(dictionary, delimiter=";")
    dictionary_data = list(dictionary_reader)
    to_sort_list = []
    for row in dictionary_data:
        to_sort_list.append(row[0])
    print("\nAPPELLATIONS IN ALPHABETICAL ORDER:\n")
    for appellation in sorted(to_sort_list):
        print("{:>20}".format(appellation))
    print("")
    dictionary.close()


def show_by_letter(letter):
    dictionary = open("dictionary.csv", "r")
    dictionary_reader = dictionary_reader = csv.reader(dictionary, delimiter=";")
    dictionary_data = list(dictionary_reader)
    available_definitions = []
    for row in dictionary_data:
        if row[0][0].lower() == letter:
            available_definitions.append(row[1])
    print("\nAVAILABLE DEFINITIONS"
          "\nFOR APPELLATIONS STARTING ON LETTER: {}\n".format(letter.upper()))
    for definition in available_definitions:
        print("{}\n".format(definition))
    dictionary.close()


def continue_or_exit():
    answer = input("Another operation ?\nType \"yes\" or \"no\": ").lower()
    while not match("^yes$|^no$", answer):
        answer = input("\nWrong input. \nType \"yes\" or \"no\": ").lower()
    return answer


dictionary()
