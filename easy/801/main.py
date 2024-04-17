from typing import List
import argparse
import math
import random

def calc_sevenish_list(num: int) -> List[int]:
    """ """
    sevenish_list = []
    if num == 0:
        return []

    sevenish_list.append(pow(7,0))
    num -= 1

    power = 1
    next = "power"
    while num > 0:
        if next == "power":
            sevenish_list.append(pow(7,power))
            power += 1
            next = "sum"
        else:
            sevenish_list.append(sevenish_list[-2] + sevenish_list[-1])
            next = "power"

        num -= 1
    return sevenish_list



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("num", type=int, help="Number of sevenish elements to calculate.")
    args = parser.parse_args()
   
    print(calc_sevenish_list(args.num))

if __name__ == "__main__":
    main()