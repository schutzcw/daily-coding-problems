import argparse
import math

from typing import NamedTuple, Tuple


class Result(NamedTuple):
    val: float
    string: str


def calc_term(frac: float) -> Result:
    """ """
    term = math.ceil(1 / frac)
    return Result(1 / term, f"1/{term}")


def main():
    """ """
    parser = argparse.ArgumentParser()
    parser.add_argument("fraction", help="fraction of the form N/M, where M > N")
    args = parser.parse_args()

    tokens = args.fraction.split("/")
    if len(tokens) != 2:
        raise RuntimeError("invalid input")

    n = int(tokens[0])
    m = int(tokens[1])
    remaining = n / m
    eps = 1e9
    answer = ""
    while remaining > (1 / eps):
        result = calc_term(remaining)
        if answer == "":
            answer = result.string
        else:
            answer += f" + {result.string}"
        remaining -= result.val
    print(f"{args.fraction} = {answer}")


if __name__ == "__main__":
    main()
