import argparse
import os
import pathlib
import sys
import functools


@functools.cache
def compute(input_str: str) -> str:
    output = []
    last = None
    for i in range(len(input_str)):
        chr = input_str[i]
        if chr != last:
            output.append(1)
            output.append(chr)
        else:
            output[-2] += 1
        last = chr
    return "".join([str(c) for c in output])


def main() -> None:
    """
    description

    :param name:
    :return
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("term", type=int, help="term number to print out")
    args = parser.parse_args()

    input_str = "1"
    print(input_str)
    for i in range(1, args.term):
        input_str = compute(input_str)
        print(input_str)

if __name__ == "__main__":
    main()
