from typing import List

def get_furthest_distance(mice: List[int], holes: List[int]):
    mice.sort()
    holes.sort()

    max_distance = 0
    for i in range(len(mice)):
        distance = abs(mice[i] - holes[i])
        if distance > max_distance:
            max_distance = distance
    return max_distance

def main():
    MICE = [1, 4, 9, 15]
    HOLES = [10, -5, 0, 16]
    max_distance = get_furthest_distance(MICE, HOLES)
    print(f"Max Distance: {max_distance}")

if __name__ == "__main__":
    main()