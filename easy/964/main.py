###
# Note: You did iterative approach when you could've just done modulo
###

import argparse


class DataStruct():
    
    def __init__(self, n: int) -> None:
        """ """
        self._arr = [None] * n
        self._next_idx = 0  # zero-indexed index

    def record(self, order_id: int) -> None:
        """Adds the order_id into the log"""
        self._arr[self._next_idx] = order_id
        self._next_idx += 1
        if self._next_idx == len(self._arr):
            self._next_idx = 0
    
    def get_last(self, i: int) -> (int | None):
        """ gets the ith last element from the log. i is guaranteed to be smaller than or equal to
        N"""
        last_idx = self._next_idx - 1
        last_idx = last_idx if last_idx >= 0 else len(self._arr) - 1
        while i > 0:
            i -= 1
            last_idx -= 1
            if last_idx < 0:
                last_idx = len(self._arr) - 1
        print(self._arr[last_idx])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", required=True, type=int, help="Number of elements in the log")
    args = parser.parse_args()

    print(args.n)
    d = DataStruct(args.n)
    for i in range(15):
        d.record(i)

    d.get_last(4)

if __name__ == "__main__":
    main()