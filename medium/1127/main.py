import math
import random

def main(string: str):
    """ """

    # count number of distinct letters
    # TODO: How are set's implemented in python? Is it red-black tree or hashmap?
    unq_char_set = set()
    for letter in string:
        unq_char_set.add(letter)
    print(f"# distinct characters: {len(unq_char_set)}")

    start_idx = 0
    end_idx = 0
    char_map: dict[str, int] = dict()
    while end_idx < len(string):
        if len(char_map) < len(unq_char_set):
            end_idx += 1




if __name__ == "__main__":
    string = "jiujitsu"
    main(string)