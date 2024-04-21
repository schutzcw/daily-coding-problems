import random
from typing import List


def longest_consecutive_sequence(list_: List[int]) -> List[int]:
    """ """
    set_ = set(list_)
    longest_vals: List[int] = []
    while len(set_) > 0:
        current_vals: List[int] = []
        start = set_.pop()
        current_vals.append(start)
        val = start - 1
        while val in set_:
            set_.remove(val)
            current_vals.append(val)
            val -= 1
        val = start + 1
        while val in set_:
            set_.remove(val)
            current_vals.append(val)
            val += 1

        if len(current_vals) > len(longest_vals):
            longest_vals = current_vals

    return longest_vals



def test_case():
    """"""
    list_ = [100, 4, 200, 1, 3, 2]
    longest_seq = longest_consecutive_sequence(list_)
    print(longest_seq)
    print(len(longest_seq))


def random_case():
    import timeit
    i = 100
    while i < 100_000_000:
        list_ = random.sample(range(0, 1000_000_000), i)
        time_sec = timeit.timeit(lambda: longest_consecutive_sequence(list_), number=3)
        print(f"{i:10d} - {time_sec}")
        i = i * 10


def main():
    #test_case()
    random_case()

if __name__ == "__main__":
    main()