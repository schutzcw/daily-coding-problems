import random
from typing import List, NamedTuple

class UnsortedIndices(NamedTuple):
    start: int = -1
    end: int = -1

# runtime of O(n). 4*O(n)
def find_unsorted_window(lst: list[int]) -> UnsortedIndices:
    """ """

    print(lst)

    if len(lst) == 0:
        return UnsortedIndices()

    prev_val = lst[0]
    for idx1, val in enumerate(lst):
        if val < prev_val:
            idx1 -= 1
            break
        prev_val = val

    prev_val = lst[-1]
    for idx2 in range(len(lst)-2,-1,-1):
        if lst[idx2] > prev_val:
            idx2 += 1
            break
        prev_val = lst[idx2]

    smallest = min(lst[idx1:idx2+1])
    largest = max(lst[idx1:idx2+1])

    for idx, val in enumerate(lst[:idx1+1]):
        if smallest < val:
            idx1 = idx
            break
    
    for idx in range(len(lst) - 1, -1, -1):
        if largest > lst[idx]:
            idx2 = idx
            break
    
    return UnsortedIndices(idx1, idx2)

def generate_random_list(n: int, lower_bound: int = 0, upper_bound: int = 100) -> list[int]:
    """ """
    return [random.randint(lower_bound, upper_bound) for _ in range(n)]

def main():
    # print(find_unsorted_window([3,7,5,6,9]))
    # print(find_unsorted_window([3,7,5,4,6,9]))
    print(find_unsorted_window(generate_random_list(10)))

if __name__ == "__main__":
    main()