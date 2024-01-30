from typing import List

def ex1() -> List[int]:
    return [3, 4, -1, 1]

def ex2() -> List[int]:
    return [1, 2, 0]

def find_lowest_positive_int_missing(arr) -> int:
    
    for idx, val in enumerate(arr):
        if val < 0:
            continue
        elif val > len(arr):
            arr[idx] = -1
            continue
        else:
            tmp = arr[val]
            arr[val] = val  
    
if __name__ == "__main__":
    TODO