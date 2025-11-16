import argparse
import os
import pathlib
import sys

def main(min_val, max_val) -> None:
    """
    description

    :param name:
    :return
    """
    diff = max_val - min_val

    print(f"max_val = {max_val} = {max_val:30b}")
    print(f"min_val = {min_val} = {min_val:30b}")
    print(f"diff    = {diff}    = {diff:30b}")

    # brute
    digits = len(bin(max_val)) - 2 # -2 for leading '0b'
    bin_str = "1"*digits
    result = int(bin_str,2)
    print(f"result: {bin(result)}")
    for val in range(min_val, max_val+1):
        print(f"val   : {bin(val)}")
        result = result & val
        print(f"result: {bin(result)}")
        print("*"*10)
    print(f"result: {bin(result)}")
    # convert to binary and strip off leading '0b'
    #N = bin(N)[2:]
    #M = bin(M)[2:]



def rangeBitwiseAnd(m, n):
    """
    Returns the bitwise AND of all integers between m and n, inclusive.

    Args:
        m: Start of range (inclusive)
        n: End of range (inclusive)

    Returns:
        Bitwise AND of all numbers in [m, n]
    """
    shift = 0
    # Find the common prefix of m and n
    while m != n:
        m >>= 1
        n >>= 1
        shift += 1
    # Shift back to get the result
    return m << shift


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("min_val", type=int, help="M")
    parser.add_argument("max_val", type=int, help="N")
    args = parser.parse_args()

    main(args.min_val, args.max_val)
    result = rangeBitwiseAnd(args.min_val, args.max_val)
    print(bin(result))
