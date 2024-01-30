import argparse
import math
import random

from typing import List, NamedTuple

class XORMax(NamedTuple):
    xor: int
    val1: int
    val2: int


def brute_force(list_: List[int]) -> int:
    """
    """

    max_ = XORMax(0,0,0)
    for i in range(len(list_)):
        for j in range(i+1, len(list_)):
            val1 = list_[i]
            val2 = list_[j]
            xor =  val1 ^ val2
            if xor > max_.xor:
                max_ = XORMax(xor, val1, val2)
    return max_

def generate_test_case(n: int, max_: int) -> List[int]:
    """
    """
    list_ = []
    for i in range(n):
        list_.append(random.randint(0,max_))
    return list_


def main():
    """ """

    parser = argparse.ArgumentParser()
    parser.add_argument("--length", type=int, default=20, help="length of array of random ints")
    parser.add_argument("--max-val", type=int, default=1000, help="max value of any value in the array")
    args = parser.parse_args()

    list_ = generate_test_case(args.length, args.max_val)
    max_xor = brute_force(list_)
    print(max_xor)
    other_technique(list_)

if __name__ == "__main__":
    main()