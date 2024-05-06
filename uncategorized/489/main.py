from typing import Dict

example = [5, 1, 3, 5, 2, 3, 4, 1]
answer = [5, 2, 3, 4, 1]

def main():
    """ """

    arr = example
    if len(arr) == 0:
        return []
    
    # maps from value seen to the index it was first seen
    val_map: Dict[int, int] = {arr[0]: 0}
    
    length, max_length = 0, 0
    start_idx, max_idx = 0, 0
    
    idx = 0
    while idx <= len(arr) - 1:
        val = arr[idx]
        if val in val_map:
            if length > max_length:
                max_length = length
                max_idx = start_idx

            start_idx = val_map[val] + 1
            idx = start_idx

            length = 0
            val_map = {}

            print(f"duplicate on {val}. New start idx: {start_idx}")
        else:
            val_map[val] = idx
            length += 1
        idx += 1
    
    if length > max_length:
        max_length = length
        max_idx = start_idx
    
    print(f"{arr[max_idx:max_idx + max_length + 1]}")


if __name__ == "__main__":
    main()
