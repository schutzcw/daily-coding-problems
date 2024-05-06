from typing import List, Union

def fixed_point(input_list: List[int]) -> Union[int, bool]:
    for idx, val in enumerate(input_list):
        if idx == val:
            return idx
    return False

def main():
    print(fixed_point([-6, 0, 2, 40]))
    print(fixed_point([1, 5, 7, 8]))

if __name__ == "__main__":
    main()