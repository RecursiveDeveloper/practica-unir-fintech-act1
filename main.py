"""
License: Apache
Organization: UNIR
"""

import os, sys

DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False

def sort_list(items, ascending=True):
    if not isinstance(items, list):
        raise RuntimeError(f"It can't be sorted {type(items)}")
    return sorted(items, reverse=(not ascending))

def remove_duplicates_from_list(items):
    return list(set(items))

if __name__ == "__main__":
    filename = DEFAULT_FILENAME
    remove_duplicates = DEFAULT_DUPLICATES
    if len(sys.argv) == 3:
        filename = sys.argv[1]
        remove_duplicates = sys.argv[2].lower() == "yes"
    else:
        print("Filename must be declared as the first argument")
        print("The second argument declares if duplicated words must be removed")
        sys.exit(1)

    print(f"Words from {filename} will be read")
    file_path = os.path.join(".", filename)
    if os.path.isfile(file_path):
        word_list = []
        with open(file_path, "r") as file:
            for line in file:
                word_list.append(line.strip())
    else:
        print(f"The file {filename} doesn't exists")
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    if remove_duplicates:
        word_list = remove_duplicates_from_list(word_list)

    print(sort_list(word_list))