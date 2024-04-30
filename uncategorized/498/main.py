from typing import List

def subsort_indices(arr: List[int]):
    """"""
    start_idx = -1
    for i, val in enumerate(arr):
        print(f"i: {i}, val: {val}")
        for j, comp in enumerate(arr[i+1:], i):
            print(f"\tj: {j}, comp: {comp}")
            if comp < val:
                print(f"\tSettings start_idx")
                start_idx = i
                break
        if start_idx != -1:
            break

    print(f"start idx: {start_idx}")

    end_idx = -1
    reverse = arr[::-1]
    for i, val in enumerate(reverse):
        print(f"i: {i}, val: {val}")
        for j, comp in enumerate(reverse[i+1:], i):
            print(f"\tj: {j}, comp: {comp}")
            if comp > val:
                print(f"\tSettings end_idx")
                end_idx = i
                break
        if end_idx != -1:
            break
    end_idx = len(arr) - 1 - end_idx
    print(f"end idx: {end_idx}")

def test_case():
    arr = [1, 7, 8, 9, 2, 3, 4]
    # arr = [3, 7, 5, 6, 9]
    # arr = [3,7,5,6,1,9,4]
    print(arr)
    subsort_indices(arr)




if __name__ == "__main__":
    test_case()