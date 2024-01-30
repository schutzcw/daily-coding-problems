import argparse
from typing import List, Optional

from doubly_linked_list import DoublyLinkedList


def find_celeb(knows: List[List[int]]) -> int:
    """Given the knows matrix. Figure out which person is the celebrity in O(n) time. The approach
    is to compare the first person to the second. If the first knows the second, the first cannot be
    the celeb b/c the celeb doesn't know anyone. If the first does not know the second, then the
    second cannot be the celeb b/c everyone knows the celeb. This is O(n) b/c one person is
    eliminated for as the possible celeb for the `knows()` call.

    Args:
        knows (List[List[int]]): [N x M] square matrix where (n,m) == 1 means that person n knows
        person m.

    Returns:
        int: The index of the celebrity.
    """

    size = len(knows)
    dll = DoublyLinkedList()
    for i in range(size):
        dll.add_back(i)

    knows_calls = 0
    while dll.size() != 1:
        first = dll.head.val
        second = dll.head.next.val

        # first cannot be celeb. Remove first
        knows_calls += 1
        if knows[first][second] == 1:
            dll.remove_first(first)
        else: # second cannot be celeb. Remove second
            dll.remove_first(second)

    print(f"knows_calls: {knows_calls}")
    print(f"celeb guess: {dll.head.val}")
    return dll.head.val


def create_knows_matrix(size: int, seed: Optional[int] = None) -> List[List[int]]:
    """Create a [size x size] matrix of booleans, where element (n,m) is True is person `n` knows
    person `m`. Otherwise person `n` does not know person `m`. The matrix must have identity be
    True. For one and only one row, the celeb, all other columns must be False. The celeb column `m`
    must be all True. There are no other constraints on the matrix.

    Args:
        size (int): The number of people at the party
        seed (int): The seed used to generate the `knows` matrix

    Returns:
        List[List[int]]: The `knows` matrix
    """

    import random
    import time
    if seed is None:
        seed = int(time.time())
    print(f"seed: {seed}")
    random.seed(seed)

    # celeb is value in [0, size -1] range
    celeb = random.randrange(0, size)
    knows = [[random.choice([0, 1]) for _ in range(size)] for _ in range(size)]
    
    # celeb does not know anyone else
    knows[celeb] = [0] * size

    # everyone knows the celeb
    for row in range(size):
        knows[row][celeb] = 1
    
    # everyone knows themselves
    for idx in range(size):
        knows[idx][idx] = 1

    return celeb, knows


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--size", type=int, default=10, help="Number of people at the party")
    parser.add_argument("--seed", type=int, default=None, help="Seed for random number generator")
    args = parser.parse_args()

    celeb, knows_matrix = create_knows_matrix(args.size, args.seed)
    print(f"Actual Celeb: {celeb}")
    for row in knows_matrix:
        print(row)
    
    guess = find_celeb(knows_matrix)
    result = "CORRECT!" if guess == celeb else "Incorrect..."
    print(result)


if __name__ == "__main__":
    main()
