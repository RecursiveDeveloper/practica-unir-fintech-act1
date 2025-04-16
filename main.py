"""
License: Apache
Organization: UNIR
"""

import os, sys

DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False
DEFAULT_ASCENDING = True

def sort_list(items, ascending=True):
    if not isinstance(items, list):
        raise RuntimeError(f"It can't be sorted {type(items)}")
    return sorted(items, reverse=(not ascending))

def remove_duplicates_from_list(items):
    return list(set(items))

if __name__ == "__main__":
    filename = DEFAULT_FILENAME
    remove_duplicates = DEFAULT_DUPLICATES
    ascending_order = DEFAULT_ASCENDING
    if len(sys.argv) == 4:
        filename = sys.argv[1]
        remove_duplicates = sys.argv[2].lower() == "yes"
        ascending_order = sys.argv[3].lower() == "asc"
    else:
        print("Se debe indicar el fichero como primer argumento")
        print("El segundo argumento indica si se quieren eliminar duplicados")
        print("El tercer argumento indica si se quieren ordenar 'asc' o 'desc' para orden ascendente o descendente")
        sys.exit(1)

    print(f"Se leerán las palabras del fichero {filename}")
    print(f"Orden: {'ascendente' if ascending_order else 'descendente'}")

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
    print(sort_list(word_list, ascending=ascending_order))