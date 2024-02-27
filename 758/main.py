from typing import List


def rotate(l: List[int], k: int):
    LENGTH = len(l)
    for idx in range(LENGTH-k):
        new_idx = idx - k
        if new_idx < 0:
            new_idx = new_idx + LENGTH
        tmp = l[new_idx]
        l[new_idx] = l[idx]
        l[idx] = tmp
    print(l)


def main():
    rotate([1, 2, 3, 4, 5, 6], 2)


if __name__ == "__main__":
    main()
