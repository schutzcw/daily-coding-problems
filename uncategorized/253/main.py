import argparse
import math


def main():
    """ """
    parser = argparse.ArgumentParser()
    parser.add_argument("string", help="String to zigzag")
    parser.add_argument("n", type=int, help="number of lines to use")
    args = parser.parse_args()

    row = [" " for i in range(len(args.string))]
    rows = [row.copy() for i in range(args.n)]

    val = 0
    direction = 1  # 1 for up, -1 for down
    for i, l in enumerate(args.string):
        if val == 0:
            direction = 1
        elif val == (args.n - 1):
            direction = -1
        rows[val][i] = l
        val = val + (1 * direction)

    for row in rows:
        print("".join(row))


if __name__ == "__main__":
    main()

