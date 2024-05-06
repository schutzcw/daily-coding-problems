from typing import List
import math
import random

KAPREKARS_CONSTANT = 6174

def generate_four_digit() -> int:
    
    values = []
    for i in range(4):
        digit = str(math.floor(10*random.random()))
        values.append(digit)
    return int("".join(values))

def get_digits(value: int) -> List[str]:
    return list[str(value)]

if __name__ == "__main__":
    found = False
    while not found:
        number = generate_four_digit()
        val_str = str(number)
        if len(val_str) != 4:
            continue
        if len(set(val_str)) < 2:
            continue
        found = True

    iterations = 0
    print(f"starting number: {number}")
    while number != KAPREKARS_CONSTANT:
        str_list = list(str(number))
        ascend = int("".join(sorted(str_list)))
        descend = int("".join(sorted(str_list, reverse=True)))
        number = descend - ascend
        print(f"{descend} - {ascend} = {number}")
        iterations += 1
    print(f"Iterations: {iterations}")
        
