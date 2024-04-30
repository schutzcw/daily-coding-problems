#!/usr/bin/env python3
#   SEND
# + MORE
# --------
#  MONEY
import argparse
import os
import pdb

from typing import List

# TODO: uniqueness of digits
# TODO: review backtracking. It might not be valid
def add(a: int, b: int, c: int, carry: int = 0) -> bool:
    """ Return True is a+b=c, otherwise False """
    v = a + b + carry
    return v == c


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="Path to file containing input crypto-math")
    args = parser.parse_args()

    if not os.path.isfile(args.file):
        raise RuntimeError(f"Not a file: {args.file}")

    # read
    with open(args.file, "rt") as F:
        data = F.read().split("\n")
        data = [d.strip() for d in data]
    del data[2]

    ### format ###

    # remove spaces, remove operator, get max width
    length = 0
    for i, _ in enumerate(data):
        line = data[i].replace("+", "")
        data[i] = line.replace(" ", "")
        if len(data[i]) > length:
            length = len(data[i])

    data = [d.rjust(length) for d in data]

    # debug print
    for d in data:
        print(d)

    # initialize backtrace lists
    chars = []
    idx_map = {}  # map from variable name to index in chars/vals list
    vals = []

    ordered_cols = [i for i in zip(data[0][::-1], data[1][::-1], data[2][::-1])]
    for col in ordered_cols:
        for char in col:
            if (char not in chars) and (char != " "):
                idx_map[char] = len(chars)
                chars.append(char)
                vals.append(0)

    for col in ordered_cols:
        print(col)
    print(chars)

    # leftmost character on each line should be one
    for d in data:
        idx = idx_map[d.strip()[0]]
        vals[idx] = 1

    min_vals = vals.copy()

    def eval_good(vals: List[int], idxs: List[int], carry: int) -> bool:
        """ return true on success """

        # -1 for idx means a space in the addition, so use 0
        try:
            _vals = [vals[idx] if idx > 0 else 0 for idx in idxs]
            return True if (_vals[0] + _vals[1] + carry == _vals[2]) else False
        except Exception as e:
            pdb.set_trace()

    carry = 0  # TODO: Test

    g_idx = 1  # assume all before this are correct
    while True:
        print(f"g_idx: {g_idx}")
        print(vals)
        if g_idx < 0:
            pdb.set_trace()
            raise RuntimeError("g_idx < 0 means no valid solution")
        if vals[g_idx] > 9:
            pdb.set_trace()
            raise RuntimeError("vals[g_idx] > 9")
        for col in ordered_cols:
            print(col)
            print(f"\tcarry={carry}")
            print(f"\t{col[0]} + {col[1]} = {col[2]}")
            idxs = tuple([idx_map[v] if v != " " else -1 for v in col])

            for idx in idxs:
                # assume lower indices are correct
                valid = True
                if idx < g_idx:
                    print(f"\tSkipping already set {chars[idx]}")
                    continue
                while not eval_good(vals, idxs, carry):
                    vals[idx] += 1
                    if vals[idx] > 9:
                        print(f"\t{chars[idx]} == 10. valid = False")
                        valid = False
                        break
                if valid:
                    print(f"\tFound valid idx={idx}, char={chars[idx]}, val={vals[idx]}.")
                    g_idx += 1
                    print(f"\tIncremented g_idx={g_idx}")
                else:
                    break

            if not valid:
                for i in range(g_idx, len(chars)):
                    vals[i] = min_vals[i]
                g_idx -= 1
                vals[g_idx] += 1
                break
            else:
                if vals[idxs[0]] + vals[idxs[1]] > 9:
                    carry = 1
                else:
                    carry = 0
