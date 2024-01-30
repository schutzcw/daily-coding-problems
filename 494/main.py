import argparse
import random
from typing import List


def max_subarray(lst: List[int]) -> int:
    """ """
    if len(lst) == 0:
        return 0

    sums: List[int] = []
    sum_ = 0
    for val in lst:
        if val < 0:
            sums.append(sum_)
            sum_  = 0
        else:
            sum_ += val
    sums.append(sum_)
    if len(sums) > 1:
        sums.append(sums[0] + sums[-1])
    return max(sums)


def test_cases():
    vals = [8, -1, 3, 4]
    print(max_subarray(vals))
    vals = [-4, 5, 1, 0]
    print(max_subarray(vals))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("size", type=int, help="Size of random int array")
    args = parser.parse_args()

    vals: List[int] = []
    for _ in range(args.size):
        vals.append(random.randrange(-25, 75))
    print(vals)
    print(max_subarray(vals))


if __name__ == "__main__":
    main()