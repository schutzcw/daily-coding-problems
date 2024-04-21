#!/usr/bin/env python3

import argparse

from typing import List


def purge(l: List[int], k: int, rnd: int = 1) -> List[int]:
    """ """
    print(f"len={len(l)}, k={k}")
    if len(l) < k:
        print("HERE")
        return l

    survived = [v for (i, v) in enumerate(l, start=1) if (i % k) > 0]
    print(f"Survived round {rnd} : {survived}")
    return purge(survived, k, rnd + 1)


def main():
    """ """
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", required=True, type=int, help="Total number of prisoners")
    parser.add_argument("-k", required=True, type=int, help="Execute every kth")
    args = parser.parse_args()

    l = [i for i in range(1, args.n)]
    print(f"Original: {l}")

    purge(l, args.k)


if __name__ == "__main__":
    main()

