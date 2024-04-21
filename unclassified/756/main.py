from collections import defaultdict
from typing import Dict, List, NamedTuple
import random


NUM_TO_STR_MAP = {0: "zero",
                  1: "one",
                  2: "two",
                  3: "three",
                  4: "four",
                  5: "five",
                  6: "six",
                  7: "seven",
                  8: "eight",
                  9: "nine"}

class RandomAnagram(NamedTuple):
    """ """
    solution: str
    anagram: str


def generate_random() -> RandomAnagram:
    """Return a random number anagram. The anagram will contain between 2 and 15 numbers,
    inclusive.
    
    Return: A RandomAnagam object that contains the anagram and the correct solution.
    """
    DIGITS = int(random.uniform(2,16))
    numbers = []
    string = ""
    for i in range(DIGITS):
        DIGIT = int(random.uniform(0,10))
        numbers.append(DIGIT)
        string += NUM_TO_STR_MAP[DIGIT]
    
    SWAPS = 1000
    string_list = [char for char in string]
    for i in range(SWAPS):
        swap1 = int(random.uniform(0,len(string)))
        swap2 = int(random.uniform(0,len(string)))
        tmp = string_list[swap2]
        string_list[swap2] = string_list[swap1]
        string_list[swap1] = tmp
    
    numbers = sorted(numbers)
    number = "".join([str(n) for n in numbers])
    return RandomAnagram(number, string_list)


def reduce_map(input_map: Dict[str, int], answer: List[int], char_map: Dict[str, int]) -> None:
    for uniq_char in char_map:
        for _ in range(input_map[uniq_char]):
            answer.append(char_map[uniq_char])
            NUM_STRING = NUM_TO_STR_MAP[char_map[uniq_char]]
            for char in NUM_STRING:
                input_map[char] -= 1

def get_answer(string: str) -> str:
    input_map = defaultdict(int)
    for char in string:
        input_map[char] += 1

    UNIQ_LVL1 = {
        "z" : 0,
        "w" : 2,
        "u" : 4,
        "x" : 6,
        "g" : 8,
    }

    answer = []
    reduce_map(input_map, answer, UNIQ_LVL1)
    
    UNIQ_LVL2 = {
        "f": 5,
        "h": 3,
        "o": 1,
        "s": 7,

    }
    reduce_map(input_map, answer, UNIQ_LVL2)

    UNIQ_LVL3 = {
        "i": 9,
    }
    reduce_map(input_map, answer, UNIQ_LVL3)

    answer = sorted(answer)
    return "".join([str(i) for i in answer])



def main():
    for i in range(100):
        random_input = generate_random()
        print(random_input)
        answer = get_answer(random_input.anagram)
        print(random_input.solution)
        print(answer)
        if random_input.solution != answer:
            raise RuntimeError()
    print("SUCCESS")


if __name__ == "__main__":
    main()